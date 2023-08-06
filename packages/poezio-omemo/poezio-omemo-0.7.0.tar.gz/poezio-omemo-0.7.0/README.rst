Poezio OMEMO plugin
###################

**This plugin will not work with Poezio 0.12.**


This is a `Poezio <https://poez.io>`_ plugin providing OMEMO support. It
distributed separately for licensing reasons.

This plugin is very much **alpha**. It handles encryption and decryption
of OMEMO messages, but doesn't display the encryption state of messages,
and neither does it have a way to do trust management. As this plugin is
still changing often, it is recommended that users follow experimental
(master) versions of this project and its dependencies.

License
-------

This plugin is licensed under GPLv3.

Note on the underlying OMEMO library
------------------------------------

As stated in `python-xeddsa's
README <https://github.com/Syndace/python-xeddsa/blob/136b9f12c8286b9463566308963e70f090b60e50/README.md>`_,
(dependency of python-omemo), this library has not undergone any
security audits. If you have the knowledge, any help is welcome.

Please take this into consideration when using this library.

Installation
------------

As this plugin is still changing often, it is recommended that users
follow experimental (main) versions of this project and its
dependencies.

- ArchLinux (AUR):
   `poezio-omemo <https://aur.archlinux.org/packages/poezio-omemo>`_, or
   `poezio-omemo-git <https://aur.archlinux.org/packages/poezio-omemo-git>`_
- PIP: `poezio-omemo`
- Manual: `python3 setup.py install`

Common issues
-------------

This plugin is **NOT** to be placed in the Poezio plugin folder, doing
so may shadow the OMEMO library and render it inaccessible from Poezio.
This module declares itself via `pkg_resources` under the
`poezio_plugins` group.

Other possible issues when loading the plugin may be that the OMEMO
library is incorrectly setup.

In a Python interpreter::

  >>> # Is the backend OMEMO library is reachable? (success: no error, no output)
  >>> import omemo
  >>> # Is poezio_omemo reachable? (success: no error, no output)
  >>> import poezio_omemo
  >>> # Is the module probably declared in plugin entries? (success: true)
  >>> import pkg_resources
  >>> 'omemo' in map(lambda e: e.name, pkg_resources.iter_entry_points('poezio_plugins'))

If this doesn't yield any error and Poezio still can't load the plugin,
try starting it with a debug file (`-d poezio.log`) and join our
`channel <xmpp:poezio@muc.poez.io?join>`_.

Use in poezio
-------------

Once installed (see the `Installation`_ section below), you can add
`omemo` in the `plugin_autoload` configuration. See the Poezio
`documentation
<https://doc.poez.io/plugins/index.html#plugin-autoload>`_ for more
information about autoloading plugins.

TODO
----

- UI, various commands and indicators that messages are encrypted or not.
