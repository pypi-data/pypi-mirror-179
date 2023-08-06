#!/usr/bin/python3
# -*- coding: utf-8 -*-


from slpkg.configs import Configs


def usage(status: int):
    colors = Configs.colour
    color = colors()

    BOLD = color['BOLD']
    RED = color['RED']
    CYAN = color['CYAN']
    YELLOW = color['YELLOW']
    ENDC = color['ENDC']

    args = [f'{BOLD}USAGE:{ENDC} {Configs.prog_name} [{YELLOW}OPTIONS{ENDC}] [{CYAN}COMMAND{ENDC}] <packages>\n',
            f'{BOLD}DESCRIPTION:{ENDC}',
            '  Packaging tool that interacts with the SBo repository.\n',
            f'{BOLD}COMMANDS:{ENDC}',
            f'  {RED}update{ENDC}                        Update the package lists.',
            f'  {CYAN}upgrade{ENDC}                       Upgrade all the packages.',
            f'  {CYAN}check-updates{ENDC}                 Check for news on ChangeLog.txt.',
            f'  {CYAN}clean-logs{ENDC}                    Clean dependencies log tracking.',
            f'  {CYAN}clean-tmp{ENDC}                     Delete all the downloaded sources.',
            f'  {CYAN}-b, build{ENDC} <packages>          Build only the packages.',
            f'  {CYAN}-i, install{ENDC} <packages>        Build and install the packages.',
            f'  {CYAN}-d, download{ENDC} <packages>       Download only the scripts and sources.',
            f'  {CYAN}-r, remove{ENDC} <packages>         Remove installed packages.',
            f'  {CYAN}-f, find{ENDC} <packages>           Find installed packages.',
            f'  {CYAN}-w, view{ENDC} <packages>           View packages from the repository.',
            f'  {CYAN}-s, search{ENDC} <packages>         Search packages from the repository.\n',
            f'{BOLD}OPTIONS:{ENDC}',
            f'  {YELLOW}--yes{ENDC}                         Answer Yes to all questions.',
            f'  {YELLOW}--jobs{ENDC}                        Set it for multicore systems.',
            f'  {YELLOW}--resolve-off{ENDC}                 Turns off dependency resolving.',
            f'  {YELLOW}--reinstall{ENDC}                   Upgrade packages of the same version.',
            f'  {YELLOW}--skip-installed{ENDC}              Skip installed packages.\n',
            '  -h, --help                    Show this message and exit.',
            '  -v, --version                 Print version and exit.\n',
            'Edit the configuration file in the /etc/slpkg/slpkg.toml.',
            'If you need more information try to use slpkg manpage.']

    for opt in args:
        print(opt)
    raise SystemExit(status)
