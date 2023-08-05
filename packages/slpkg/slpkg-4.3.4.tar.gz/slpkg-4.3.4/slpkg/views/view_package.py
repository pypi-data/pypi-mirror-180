#!/usr/bin/python3
# -*- coding: utf-8 -*-


import urllib3

from slpkg.configs import Configs
from slpkg.models.models import SBoTable
from slpkg.queries import SBoQueries
from slpkg.models.models import session as Session


class ViewPackage:
    ''' View the repository packages. '''

    def __init__(self):
        self.session: str = Session
        self.configs: str = Configs
        self.colors: dict = self.configs.colour

    def package(self, packages):
        http = urllib3.PoolManager()
        color = self.colors()
        GREEN = color['GREEN']
        BLUE = color['BLUE']
        YELLOW = color['YELLOW']
        CYAN = color['CYAN']
        RED = color['RED']
        ENDC = color['ENDC']

        for package in packages:
            info = self.session.query(
                SBoTable.name,
                SBoTable.version,
                SBoTable.requires,
                SBoTable.download,
                SBoTable.download64,
                SBoTable.md5sum,
                SBoTable.md5sum64,
                SBoTable.files,
                SBoTable.short_description,
                SBoTable.location
            ).filter(SBoTable.name == package).first()

            readme = http.request(
                'GET', f'{self.configs.sbo_repo_url}/{info[9]}/{info[0]}/README')

            info_file = http.request(
                'GET', f'{self.configs.sbo_repo_url}/{info[9]}/{info[0]}/{info[0]}.info')

            maintainer, email, homepage = '', '', ''
            for line in info_file.data.decode().splitlines():
                if line.startswith('HOMEPAGE'):
                    homepage = line[10:-1].strip()
                if line.startswith('MAINTAINER'):
                    maintainer = line[12:-1].strip()
                if line.startswith('EMAIL'):
                    email = line[7:-1].strip()

            deps = (', '.join([f'{pkg} ({SBoQueries(pkg).version()})' for pkg in info[2].split()]))

            print(f'Name: {GREEN}{info[0]}{ENDC}\n'
                  f'Version: {GREEN}{info[1]}{ENDC}\n'
                  f'Requires: {GREEN}{deps}{ENDC}\n'
                  f'Homepage: {BLUE}{homepage}{ENDC}\n'
                  f'Download SlackBuild: {BLUE}{self.configs.sbo_repo_url}/{info[9]}/{info[0]}{self.configs.sbo_tar_suffix}{ENDC}\n'
                  f'Download sources: {BLUE}{info[3]}{ENDC}\n'
                  f'Download_x86_64 sources: {BLUE}{info[4]}{ENDC}\n'
                  f'Md5sum: {YELLOW}{info[5]}{ENDC}\n'
                  f'Md5sum_x86_64: {YELLOW}{info[6]}{ENDC}\n'
                  f'Files: {GREEN}{info[7]}{ENDC}\n'
                  f'Description: {GREEN}{info[8]}{ENDC}\n'
                  f'Slackware: {CYAN}{self.configs.sbo_repo_url.split("/")[-1]}{ENDC}\n'
                  f'Category: {RED}{info[9]}{ENDC}\n'
                  f'SBo url: {BLUE}{self.configs.sbo_repo_url}/{info[9]}/{info[0]}{ENDC}\n'
                  f'Maintainer: {YELLOW}{maintainer}{ENDC}\n'
                  f'Email: {YELLOW}{email}{ENDC}\n'
                  f'\nREADME: {CYAN}{readme.data.decode()}{ENDC}')
