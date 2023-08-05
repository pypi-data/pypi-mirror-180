#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from slpkg.configs import Configs
from slpkg.queries import SBoQueries
from slpkg.utilities import Utilities
from slpkg.blacklist import Blacklist
from slpkg.models.models import LogsDependencies
from slpkg.models.models import session as Session


class ViewMessage:
    ''' Print some messages before. '''

    def __init__(self, flags):
        self.flags: list = flags
        self.configs: str = Configs
        self.colors: dict = self.configs.colour
        self.session: str = Session
        self.utils: str = Utilities()
        self.black: list = Blacklist()

    def build_packages(self, slackbuilds: list, dependencies: list):
        print('The following packages will be build:\n')

        for sbo in slackbuilds:
            version = SBoQueries(sbo).version()
            self._view_build(sbo, version)

        if dependencies:
            print('\nDependencies:')
            for sbo in dependencies:
                version = SBoQueries(sbo).version()
                self._view_build(sbo, version)

        self._view_total(slackbuilds, dependencies, option='build')

    def install_packages(self, slackbuilds: list, dependencies: list):
        print('The following packages will be installed or upgraded:\n')

        for sbo in slackbuilds:
            version = SBoQueries(sbo).version()
            self._view_install(sbo, version)

        if dependencies:
            print('\nDependencies:')
            for sbo in dependencies:
                version = SBoQueries(sbo).version()
                self._view_install(sbo, version)

        self._view_total(slackbuilds, dependencies, option='install')

    def download_packages(self, slackbuilds: list):
        print('The following packages will be downloaded:\n')

        for sbo in slackbuilds:
            version = SBoQueries(sbo).version()
            self._view_download(sbo, version)

    def remove_packages(self, packages: list):
        print('The following packages will be removed:\n')
        self.installed_packages = []
        slackbuilds, dependencies, deps = [], [], []

        for pkg in packages:
            self._view_installed_packages(pkg)
            slackbuilds.append(pkg)

            requires = self.session.query(
                LogsDependencies.requires).filter(
                    LogsDependencies.name == pkg).first()

            if requires:
                deps.append(requires)

        if deps and '--resolve-off' not in self.flags:
            print('\nDependencies:')

            for i in range(0, len(deps)):
                for dep in deps[i][0].split():
                    self._view_installed_packages(dep)
                    dependencies.append(dep)

        self._view_total(slackbuilds, dependencies, option='remove')

        return self.installed_packages, dependencies

    def _view_download(self, sbo: str, version: str):
        color = self.colors()

        if self.utils.is_installed(f'{sbo}-'):
            print(f'[{color["YELLOW"]} download {color["ENDC"]}] -> '
                  f'{sbo}-{version}')
        else:
            print(f'[{color["CYAN"]} download {color["ENDC"]}] -> '
                  f'{sbo}-{version}')

    def _view_build(self, sbo: str, version: str):
        color = self.colors()

        if self.utils.is_installed(f'{sbo}-'):
            print(f'[{color["YELLOW"]} build {color["ENDC"]}] -> '
                  f'{sbo}-{version}')
        else:
            print(f'[{color["CYAN"]} build {color["ENDC"]}] -> '
                  f'{sbo}-{version}')

    def _view_install(self, sbo: str, version: str):
        color = self.colors()

        installed = self.utils.is_installed(f'{sbo}-')
        install, set_color = 'install', color['RED']

        if '--reinstall' in self.flags:
            install, set_color = 'upgrade', color['YELLOW']

        if installed and 'noarch' in installed:
            self.configs.os_arch = 'noarch'

        if installed:

            if '--reinstall' not in self.flags:
                install = 'installed'

            print(f'[{set_color} {install} {color["ENDC"]}] -> '
                  f'{sbo}-{version} {set_color}'
                  f'({installed.split(self.configs.os_arch)[0][:-1].split("-")[-1]})'
                  f'{color["ENDC"]}')
        else:
            print(f'[{color["CYAN"]} install {color["ENDC"]}] -> '
                  f'{sbo}-{version}')

    def _view_installed_packages(self, name: str):
        ''' View and creates list with packages for remove. '''
        installed = os.listdir(self.configs.log_packages)
        color = self.colors()

        for package in installed:
            black = package.split('-')[0]
            if (package.startswith(f'{name}-') and
                self.configs.sbo_repo_tag in package and
                    black not in self.black.get()):
                self.installed_packages.append(package)
                print(f'[{color["RED"]} delete {color["ENDC"]}] -> {package}')

    def _view_total(self, slackbuilds: list, dependencies: list, option: str):
        color = self.colors()

        slackbuilds.extend(dependencies)
        installed = upgraded = 0

        for sbo in slackbuilds:
            if self.utils.is_installed(f'{sbo}-'):
                upgraded += 1
            else:
                installed += 1

        if option == 'install':
            print(f'\n{color["GREY"]}Total {installed} packages will be '
                  f'installed and {upgraded} will be upgraded.{color["ENDC"]}')

        elif option == 'build':
            print(f'\n{color["GREY"]}Total {installed + upgraded} packages '
                  f'will be build.{color["ENDC"]}')

        elif option == 'remove':
            print(f'\n{color["GREY"]}Total {installed + upgraded} packages '
                  f'will be removed.{color["ENDC"]}')

    def logs_packages(self, dependencies):
        print('The following logs will be removed:\n')
        color = self.colors()

        for dep in dependencies:
            print(f'{color["CYAN"]}{dep[0]}{color["ENDC"]}')
            print('  |')
            print(f'  +->{color["CYAN"]} {dep[1]}{color["ENDC"]}\n')
        print('Note: After cleaning you should remove them one by one.')

    def question(self):
        if '--yes' not in self.flags:
            answer = input('\nDo you want to continue [y/N]: ')
            print()
            if answer not in ['Y', 'y']:
                raise SystemExit()
        print()
