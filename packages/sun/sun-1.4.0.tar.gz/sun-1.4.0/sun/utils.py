#!/usr/bin/python3
# -*- coding: utf-8 -*-

# utils.py is a part of sun.

# Copyright 2015-2022 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://gitlab.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import re
import tomli
import getpass
import urllib3
from sun.__metadata__ import data


class Utilities:

    @staticmethod
    def url_open(link):
        """ Return urllib urlopen. """
        r = ''

        try:
            http = urllib3.PoolManager()
            con = http.request('GET', link)
            r = con.data.decode()
        except urllib3.exceptions.NewConnectionError as e:
            print(e)
        except AttributeError as e:
            print(e)
        except ValueError as e:
            return e
        except KeyboardInterrupt as e:
            print(e)
            raise SystemExit(1)
        except KeyError:
            print('SUN: error: ftp mirror not supported')

        return r

    @staticmethod
    def read_file(registry):
        """ Return reading file. """
        with open(registry, 'r', encoding='utf-8',
                  errors='ignore') as file_txt:
            read_file = file_txt.read()
            return read_file

    def slack_ver(self):
        """ Open a file and read the Slackware version. """
        dist = self.read_file('/etc/slackware-version')
        sv = re.findall(r'\d+', dist)

        if len(sv) > 2:
            version = ('.'.join(sv[:2]))

        else:
            version = ('.'.join(sv))

        return dist.split()[0], version

    @staticmethod
    def installed_packages():
        """ Count installed Slackware packages. """
        for pkg in os.listdir(data['pkg_path']):
            if not pkg.startswith('.'):
                yield pkg

    @staticmethod
    def read_mirrors(mirrors):
        """ Read the config file and return an uncomment line. """
        for line in mirrors.splitlines():
            line = line.lstrip()

            if line and not line.startswith('#'):
                return line

        return ''

    def mirror(self):
        """ Get mirror from slackpkg mirrors file. """
        slack_mirror = self.read_mirrors(
            self.read_file(f'{data["etc_slackpkg"]}mirrors'))

        if slack_mirror.startswith('ftp'):
            print('Please select an http/s mirror not ftp.')
            return ''

        if slack_mirror:
            return f'{slack_mirror}{data["changelog_txt"]}'

        else:
            print('You do not have any http/s mirror selected in /etc/slackpkg'
                  '/mirrors.\nPlease edit that file and uncomment ONE http/s'
                  ' mirror.\n')
            return ''

    def fetch(self):
        """ Get the ChangeLog.txt file size and counts the upgraded packages. """
        mir, r, slackpkg_last_date = self.mirror(), '', ''
        upgraded = []

        if mir:
            r = self.url_open(mir)

            if os.path.isfile(
                    f'{data["var_lib_slackpkg"]}{data["changelog_txt"]}'):
                slackpkg_last_date = self.read_file('{0}{1}'.format(
                    data['var_lib_slackpkg'],
                    data['changelog_txt'])).split('\n', 1)[0].strip()

        else:
            return upgraded

        for line in r.splitlines():
            if slackpkg_last_date == line.strip():
                break

            # This condition checks the packages
            if (line.endswith('z:  Upgraded.') or
                line.endswith('z:  Rebuilt.') or
                line.endswith('z:  Added.') or
                    line.endswith('z:  Removed.')):
                upgraded.append(line.split('/')[-1])

            # This condition checks the kernel
            if line.endswith('*:  Upgraded.') or line.endswith('*:  Rebuilt.'):
                upgraded.append(line)

        return upgraded

    @staticmethod
    def config():
        """ Return sun configuration values. """
        conf_args = {'configs':
                     {'INTERVAL': 60,
                      'STANDBY': 3}

                     }

        config_file = f'{data["conf_path"]}sun.toml'

        if os.path.isfile(config_file):
            with open(config_file, 'rb') as configs:
                conf_args = tomli.load(configs)

        return conf_args['configs']

    def os_info(self):
        """ Get the OS info. """
        stype = 'Stable'
        mir = self.mirror()

        if mir and 'current' in mir:
            stype = 'Current'

        info = (
            f'User: {getpass.getuser()}\n'
            f'OS: {self.slack_ver()[0]}\n'
            f'Version: {self.slack_ver()[1]}\n'
            f'Type: {stype}\n'
            f'Arch: {data["arch"]}\n'
            f'Packages: {len(list(self.installed_packages()))}\n'
            f'Kernel: {data["kernel"]}\n'
            f'Uptime: {data["uptime"]}\n'
            '[Memory]\n'
            f'Free: {data["mem"][9]}, Used: {data["mem"][8]}, '
            f'Total: {data["mem"][7]}\n'
            '[Disk]\n'
            f'Free: {data["disk"][2] // (2**30)}Gi, Used: '
            f'{data["disk"][1] // (2**30)}Gi, '
            f'Total: {data["disk"][0] // (2**30)}Gi\n'
            f'[Processor]\n'
            f'CPU: {data["cpu"]}'
            )

        return info
