.. contents:: Table of Contents:

About
-----

Let's SUN!


SUN (Slackware Update Notifier) is a tray notification applet for informing about
package updates in Slackware and CLI tool for monitoring upgraded packages.

.. image:: https://gitlab.com/dslackw/images/raw/master/sun/sun.png
    :target: https://gitlab.com/dslackw/sun

How works
---------

SUN reads the two dates of ChangeLog.txt files on the server and local by counting
how many packages have been upgraded, rebuilt or added.

SUN works with `slackpkg <http://www.slackpkg.org/>`_
 

Installing
----------

.. code-block:: bash

    Required root privileges

    $ tar xvf sun-1.4.0.tar.gz
    $ cd sun-1.4.0
    $ ./install.sh

    Installed as Slackware package


Requires
--------

.. code-block:: bash

    python-toml >= 0.10.2


Usage
-----

| Choose ONE http mirror from '/etc/slackpkg/mirrors' file.
| NOTE: ftp mirrors not supported.


GTK Icon
--------

.. image:: https://gitlab.com/dslackw/images/raw/master/sun/gtk_daemon.png
   :target: https://gitlab.com/dslackw/sun

.. image:: https://gitlab.com/dslackw/images/raw/master/sun/check_updates.png
   :target: https://gitlab.com/dslackw/sun

.. image:: https://gitlab.com/dslackw/images/raw/master/sun/sun_running.png
   :target: https://gitlab.com/dslackw/sun

CLI
---

.. code-block:: bash

    $ sun help
    SUN (Slackware Update Notifier) - Version: 1.4.0

    Usage: sun [OPTIONS]

    Optional arguments:
      help       Display this help and exit.
      start      Start sun daemon.
      stop       Stop sun daemon.
      restart    Restart sun daemon.
      check      Check for software updates.
      status     Sun daemon status.
      info       Os information.

    Start GTK icon from the terminal: sun start --gtk


    $ sun start
    Starting SUN daemon:  /usr/bin/sun_daemon &


    $ sun check
    3 software updates are available

    samba-4.1.17-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-firefox-31.5.0esr-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-thunderbird-31.5.0-x86_64-1_slack14.1.txz:  Upgraded.


    $ sun stop
    Stopping SUN daemon:  /usr/bin/sun_daemon


    $ sun status
    SUN is not running


Daemon autostart
----------------

If you want SUN to start automatically, run $ /usr/sbin/sun_daemon-enable.sh and /usr/sbin/sun_daemon-disable.sh to disable respectively.


Configuration files
-------------------

.. code-block:: bash

    /etc/sun/sun.toml
        General configuration of sun


Donate
------

If you feel satisfied with this project and want to thanks me make a donation.

.. image:: https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png
   :target: https://www.paypal.me/dslackw


Copyright
---------

- Copyright 2015-2022 © Dimitris Zlatanidis
- Slackware® is a Registered Trademark of Patrick Volkerding.
- Linux is a Registered Trademark of Linus Torvalds.
