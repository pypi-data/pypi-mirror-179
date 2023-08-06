#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
from dataclasses import dataclass
from slpkg.configs import Configs


@dataclass
class FindInstalled:
    log_packages: str = Configs.log_packages
    colors: dict = Configs.colour
    sbo_repo_tag: str = Configs.sbo_repo_tag

    def find(self, packages: list):
        matching = []

        print(f'The list below shows the packages '
              f'that contains \'{", ".join([p for p in packages])}\' files:\n')

        for pkg in packages:
            for package in os.listdir(self.log_packages):
                if pkg in package and self.sbo_repo_tag in package:
                    matching.append(package)
        self.matched(matching)

    def matched(self, matching: list):
        color = self.colors()
        if matching:
            for package in matching:
                print(f'{color["CYAN"]}{package}{color["ENDC"]}')
        else:
            print('\nDoes not match any package.\n')
