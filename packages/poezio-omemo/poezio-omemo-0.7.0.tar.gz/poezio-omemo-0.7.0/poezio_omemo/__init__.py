#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Maxime “pep” Buquet <pep@bouah.net>
#
# Distributed under terms of the GPLv3 license.

"""
    OMEMO Plugin.
"""

import os
import asyncio
import base64
import hashlib
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from poezio import colors
from poezio.plugin_e2ee import E2EEPlugin
from poezio.theming import Theme, dump_tuple
from poezio.tabs import ChatTab, DynamicConversationTab, StaticConversationTab, MucTab

try:
    from poezio.xdg import DATA_HOME
except ImportError:
    from poezio.libpoezio import XDG
    DATA_HOME = XDG.data_dir

from omemo.exceptions import MissingBundleException
from slixmpp import JID
from slixmpp.stanza import Message
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp_omemo import PluginCouldNotLoad, MissingOwnKey, NoAvailableSession
from slixmpp_omemo import UndecidedException, UntrustedException, EncryptionPrepareException
import slixmpp_omemo

log = logging.getLogger(__name__)


def jid_as_path(jid: JID) -> Path:
    """Ensure JID in folder names don't contain illegal chars for the FS"""
    jid_str = jid.bare.encode('utf-8')
    digest = hashlib.sha256(jid_str).digest()
    return Path(base64.b32encode(digest).decode('US-ASCII'))


class Plugin(E2EEPlugin):
    """OMEMO (XEP-0384) Plugin"""

    encryption_name = 'omemo'
    eme_ns = slixmpp_omemo.OMEMO_BASE_NS
    replace_body_with_eme = True
    stanza_encryption = False

    encrypted_tags = [
        (slixmpp_omemo.OMEMO_BASE_NS, 'encrypted'),
    ]

    self_muc_messages: Dict[str, str] = {}

    # TODO: Look into blind trust stuff.
    # https://gist.github.com/mar-v-in/b683220a55bc65dcdafc809be9c5d0e4
    # trust_states = {
    #     'accepted': {
    #         'verified',
    #         'accepted',
    #     }, 'rejected': {
    #         'undecided',
    #         'distrusted',
    #     },
    # }
    supported_tab_types = (DynamicConversationTab, StaticConversationTab, MucTab)

    default_config = {
        # Some MUC services may not reflect the message ids properly, in which
        # case it is better to set this option to false.
        'enable_muc': True,
        # For debugging purposes.
        'enable_reset_command': False,
    }

    def init(self) -> None:
        super().init()

        self.info = lambda i: self.api.information(i, 'Info')

        data_dir = os.path.join(
            DATA_HOME,
            'omemo',
            jid_as_path(self.core.xmpp.boundjid),
        )

        try:
            # Raise exception if folder exists so that we don't chmod again.
            os.makedirs(data_dir, mode=0o700, exist_ok=False)
        except OSError:  # Folder already exists
            pass

        try:
            self.core.xmpp.register_plugin(
                'xep_0384', {
                    'data_dir': data_dir,
                },
                module=slixmpp_omemo,
            ) # OMEMO
        except (PluginCouldNotLoad,):
            log.exception('And error occured when loading the omemo plugin.')

        asyncio.ensure_future(
            self.core.xmpp['xep_0384'].session_start(self.core.xmpp.boundjid)
        )

        if self.config.get('enable_reset_command', False):
            for tab_t in self.supported_tab_types:
                self.api.add_tab_command(
                    tab_t,
                    self.encryption_name + '_reset',
                    self.reset_session,
                    usage='<device-id>',
                    short='Caution: Resets session for the specified device-id.',
                    help='Caution: Resets session for the specified device-id.',
                )

    def display_error(self, txt) -> None:
        """Poezio logger Helper"""
        self.api.information(txt, 'Error')

    async def get_fingerprints(self, jid: JID) -> List[Tuple[str, bool]]:
        """Return fingerprints for the provided JID"""
        # XXX: Do we want to keep this here?
        self.core.information('Fetching up-to-date fingerprint information…', 'Info')
        await self.core.xmpp['xep_0384'].fetch_devices(jid)
        await self.core.xmpp['xep_0384'].fetch_bundles(jid)

        res: List[Tuple[str, bool]] = []
        if jid.bare == self.core.xmpp.boundjid.bare:
            res = [(await self.core.xmpp['xep_0384'].my_fingerprint(), True)]

        devices = await self.core.xmpp['xep_0384'].get_trust_for_jid(jid)

        # XXX: What to do with did -> None entries?
        # XXX: What to do with the active/inactive devices differenciation?
        # For now I'll merge both. We should probably display them separately
        # later on.
        devices['active'].update(devices['inactive'])
        res.extend([
            (slixmpp_omemo.fp_from_ik(trust['key']), False)
            for trust in devices['active'].values()
            if trust is not None
        ])

        return res

    @staticmethod
    def format_fingerprint(fingerprint: str, own: bool, theme: Theme) -> str:
        """
            Color fingerprint as specified in in XEP-0384 0.8.3 “§8 Security
            Considerations”.

            “When displaying the fingerprint as a hex-string, the RECOMMENDED
            way to make it easier to compare the fingerprint is to split the
            lowercase hex-string into 8 substrings of 8 chars each, then
            coloring each group of 8 lowercase hex chars using Consistent
            Color Generation (XEP-0392)”
        """
        size = len(fingerprint) // 8
        parts = map(''.join, zip(*[iter(fingerprint)]*8))
        colored_fp = ''
        for i, part in enumerate(parts):
            fg_color = colors.ccg_text_to_color(theme.ccg_palette, part)
            separator = ' '
            if i == (size // 2 - 1):
                separator = '\n'
            elif i == size - 1:
                separator = ''
            colored_fp += f'\x19{fg_color}}}{part}{separator}'
        if own:
            normal_color = dump_tuple(theme.COLOR_NORMAL_TEXT)
            colored_fp += f'\x19{normal_color}}} (this device)'
        return colored_fp

    def reset_session(self, args: str) -> None:
        """
            Command wrapper for _reset_session.
        """
        error = None
        try:
            did = int(args)
        except IndexError:
            error = 'Invalid argument for reset command.'
        except ValueError:
            error = 'Invalid device_id for reset command.'
        if error is not None:
            self.core.information(error, 'Error')
            return None

        jid = self.api.current_tab().jid
        asyncio.create_task(self._reset_session(jid, did))
        return None

    async def _reset_session(self, jid: JID, device_id: int) -> None:
        """
            Resets a session for the specified jid/device-id pair.
            Sends a heartbeat right after to ensure the recipient is aware
            we've resetted it.
        """
        log.debug('_reset_session: JID: %r, device_id: %r', jid, device_id)
        # Remove session material
        await self.core.xmpp['xep_0384'].delete_session(jid, device_id)
        # Send a heartbeat to ensure recipient is aware that the old session
        # isn't usable anymore.
        await self.core.xmpp['xep_0384'].send_heartbeat(jid, device_id)

    async def decrypt(self, message: Message, jid: Optional[JID], tab: Optional[ChatTab]) -> None:
        if jid is None:
            self.display_error('Unable to decrypt the message.')
            return None

        # XXX: This is only needed to workaround a bug in poezio (fixed in
        # 00a91774) that makes it not give us realjids. Remove when there is a
        # poezio release including it.
        # The realjid of the participant needs to be retrieved in a MUC.
        if isinstance(tab, MucTab):
            user = tab.get_user_by_name(jid.resource)
            if user is not None and user.jid != JID(''):
                jid = user.jid

        body = None
        try:
            encrypted = message['omemo_encrypted']
            body = await self.core.xmpp['xep_0384'].decrypt_message(
                encrypted,
                jid,
                # Always decrypt. Let us handle how we then warn the user.
                allow_untrusted=True,
            )
            # Heartbeats will return a None body.
            if body is not None:
                body = body.decode('utf-8')
        except (MissingOwnKey,):
            # The message is missing our own key, it was not encrypted for
            # us, and we can't decrypt it.
            if (message['type'] == 'groupchat' and
                    message['id'] in self.self_muc_messages):
                body = self.self_muc_messages.pop(message['id'])
            else:
                self.display_error(
                    'I can\'t decrypt this message as it '
                    'is not encrypted for me.'
                )
        except (NoAvailableSession,):
            # We received a message from that contained a session that we
            # don't know about (deleted session storage, etc.). We can't
            # decrypt the message, and it's going to be lost.
            # Here, as we need to initiate a new encrypted session, it is
            # best if we send an encrypted message directly. XXX: Is it
            # where we talk about self-healing messages?
            self.display_error(
                'I can\'t decrypt this message as it uses an encrypted '
                'session I don\'t know about.',
            )
        except (EncryptionPrepareException,):
            # Slixmpp tried its best, but there were errors it couldn't
            # resolve. At this point you should have seen other exceptions
            # and given a chance to resolve them already.
            self.display_error('I was not able to decrypt the message.')
        except (Exception,) as exn:
            self.display_error(f'An error occured while attempting decryption.\n{exn}')
            raise

        if body is not None:
            message['body'] = body

    async def encrypt(self, message: Message, jids: Optional[List[JID]], _tab) -> None:
        if jids is None:
            self.display_error('Unable to encrypt the message.')
            return None

        body = message['body']
        if self.config.get('enable_muc', True) and message['type'] == 'groupchat':
            self.self_muc_messages[message['id']] = body
        expect_problems = {}  # type: Dict[JID, List[int]]

        while True:
            try:
                # `encrypt_message` excepts the plaintext to be sent, a list of
                # bare JIDs to encrypt to, and optionally a dict of problems to
                # expect per bare JID.
                #
                # Note that this function returns an `<encrypted/>` object,
                # and not a full Message stanza. This combined with the
                # `recipients` parameter that requires for a list of JIDs,
                # allows you to encrypt for 1:1 as well as groupchats (MUC).
                recipients = jids
                encrypt = await self.core.xmpp['xep_0384'].encrypt_message(
                    body,
                    recipients,
                    expect_problems,
                )
                message.append(encrypt)
                return None
            except UndecidedException as exn:
                # The library prevents us from sending a message to an
                # untrusted/undecided barejid, so we need to make a decision here.
                # This is where you prompt your user to ask what to do. In
                # this bot we will automatically trust undecided recipients.
                await self.core.xmpp['xep_0384'].trust(exn.bare_jid, exn.device, exn.ik)
            # TODO: catch NoEligibleDevicesException
            except EncryptionPrepareException as exn:
                log.debug('FOO: EncryptionPrepareException: %r', exn.errors)
                for error in exn.errors:
                    if isinstance(error, MissingBundleException):
                        self.display_error(
                            f'Could not find keys for device "{error.device}" '
                            f'of recipient "{error.bare_jid}". Skipping.'
                        )
                        jid = JID(error.bare_jid)
                        device_list = expect_problems.setdefault(jid, [])
                        device_list.append(error.device)
            except (IqError, IqTimeout) as exn:
                self.display_error(
                    'An error occured while fetching information on a recipient.\n{exn}'
                )
                return None

        return None


if __name__ == '__main__':
    jid = JID(input('JID: '))
    print(jid_as_path(jid))
