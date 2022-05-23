#!/usr/bin/python3

import sys
import os
import urllib.request
import urllib.parse

def init_script():
    if os.geteuid() != 0:
        print("You need to be root to run this script.")
        sys.exit(1)
    else:
        if os.system('command -v git > /dev/null 2>&1') != 0:
            print('\033[1;31m[!] Git is not installed.\033[0m')
            print('\033[1;31m[!] Please install git to continue.\033[0m')
            sys.exit(1)
        else:
            if os.path.isfile('.version') == False:
                print('\033[1;31m[!] No version file detected.\033[0m')
                print(
                    '\033[1;31m[!] Please verify that you are in the right directory or the repository is correctly cloned.\033[0m')
                sys.exit(1)
            else:
                version = open('.version').read()
                return version

def splash(version):
    print("")
    print("\033[1;34m   ____       _       ___                   \033[0m")
    print("\033[1;34m  / __/___   (_)____ / _ \ __  __ __ _   ___ \033[0m")
    print("\033[1;34m / _/ / _ \ / //___// // // /_/ //    \ / _ \ \033[0m")
    print("\033[1;34m/___// .__//_/     /____/ \____//_/_/_// .__/\033[0m")
    print("\033[1;34m    /_/                               /_/    \033[0m\n\n")
    print("\033[1;32m+ -- -- +=[ Script by: Nysioko\033[1;m")
    print("\033[1;32m+ -- -- +=[ Version: " + version + "\033[1;m")
    print("\033[1;32m+ -- -- +=[ Last update: 23 May 2022\033[1;m")
    print("\033[1;32m+ -- -- +=[ This script is under the Unlicense\033[1;m\n")
    print("\033[1;91m[W] This script is under development, please report any bug to @Nysioko\033[0m")
    print("\033[1;91m[W] This script modify your environment, please be careful with it\033[0m\n")

def check_internet():
    try:
        urllib.request.urlopen('http://www.google.com')
        return True
    except:
        return False

def restart_script():
    print('Restarting script...\n')
    os.system('sleep 1')
    os.system('sudo python3 ./epi-dump.py')

def help_func(version):
    print('\n\033[1;32m[*] Usage:\033[0m')
    print('\033[1;32m[*] ./epi-dump.py [options]\033[0m')
    print('\n\033[1;32m[*] Options:\033[0m')
    print('\033[1;32m[*] -h to display this menu\033[0m')
    print('\033[1;32m[*] -a to execute the script in automatic mode\033[0m')
    print('\033[1;32m[*] -v to display the script version\033[0m')
    print('\033[1;32m[*] -u for checking and updating the script\033[0m')
    if len(sys.argv) == 2:
        print('\n')
        sys.exit(0)
    input('\n\033[1;32m[+] Press enter to continue...\033[0m')
    os.system("clear")
    splash(version)
    menu(version)

def is_latest_version(version):
    print('Checking script version...')
    os.system("wget -O /tmp/.version https://raw.githubusercontent.com/Nysioko/EpiDump/main/.version > /dev/null 2>&1")
    if os.path.isfile('/tmp/.version') == False:
        print(
            '\033[1;31m[!] Impossible to check version, please try again later\033[0m')
        print(
            '\033[1;31m[!] If the problem persist, please report it to @Nysioko\033[0m')
        sys.exit(1)
    online_version = open("/tmp/.version").read()

    if online_version == version:
        print(
            '\033[1;32m[+] You are using the latest version of the script.\033[0m\n')
        os.system('rm /tmp/.version')
    else:
        if (version > online_version):
            print(
                '\033[1;31m[!] This version is too highest in comparison to the online version.\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
            os.system('rm /tmp/.version')
            # restart_script()
        else:
            print(
                '\033[1;31m[!] You are not using the latest version of the script.\033[0m')
            print('\033[1;31m[!] Actual version: \033[1;32m' +
                  version + '\033[0m')
            print('\033[1;31m[!] Latest version: \033[1;32m' +
                  open("/tmp/.version").read() + '\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
            os.system('rm /tmp/.version')
            # restart_script()

def detect_package_manager():
    print('\nDetecting package manager...')
    print('Package manager detected: ', end='')
    package_manager = 'unknown'
    if os.system('command -v apt > /dev/null 2>&1') == 0:
        print('\033[1;32mapt\033[0m\n')
        package_manager = 'apt'
        return package_manager
    elif os.system('command -v yum > /dev/null 2>&1') == 0:
        print('\033[1;32myum\033[0m\n')
        package_manager = 'yum'
        return package_manager
    elif os.system('command -v dnf > /dev/null 2>&1') == 0:
        print('\033[1;32mdnf\033[0m\n')
        package_manager = 'dnf'
        return package_manager
    elif os.system('command -v pacman > /dev/null 2>&1') == 0:
        print('\033[1;32mpacman\033[0m\n')
        package_manager = 'pacman'
        return package_manager
    else:
        print('\033[1;31mUnknown\033[0m')
        return package_manager

def ask_install_missing_package(package_manager, i):
    print('\033[1;33m[!] Do you want to install them now? (y/n)\033[0m')
    answer = input('\033[1;33m[?] Answer: \033[0m')
    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == 'YES':
        if (package_manager == 'pacman'):
            os.system('sudo pacman -S ' + i + ' > /dev/null 2>&1')
        else:
            os.system('sudo ' + package_manager +
                      ' install ' + i + ' > /dev/null 2>&1')
            if os.system('command -v ' + i + ' > /dev/null 2>&1') == 0:
                print('\n\033[1;32m[+] ' + i +
                      ' successfully installed.\033[0m')
            else:
                print('\n\033[1;31m[!] ' + i + ' not installed.\033[0m\n')
                sys.exit(1)
    elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No' or answer == 'NO':
        print(
            '\033[1;31m[!] Please install the missing dependancies and restart the script.\033[0m')
        sys.exit(1)
    else:
        print('\n\033[1;31m[!] Please answer with y or n.\033[0m\n')
        ask_install_missing_package(package_manager, i)

def check_dependencies(package_manager):
    dependancies = ['wget', 'curl', 'gcc', 'g++', 'cmatrix']
    print('Checking dependencies...')

    for i in dependancies:
        if os.system('command -v ' + i + ' > /dev/null 2>&1') == 0:
            print('\033[1;32m' + i + '\033[0m', end='')
            if i != dependancies[-1]:
                print('\033[1;32m, \033[0m', end='')
            if i == dependancies[-1]:
                print('\n')
        else:
            print('\033[1;31m' + i + '\033[0m\n')
            print('\033[1;33m[!] You need to install "' +
                  i + '" to continue.\033[0m')
            ask_install_missing_package(package_manager, i)

def about(version):
    print("\n\033[1;32m+ -- -- +=[ Script by: Nysioko\033[1;m")
    print("\033[1;32m+ -- -- +=[ Version: " + version + "\033[1;m")
    print("\033[1;32m+ -- -- +=[ Last update: 19 May 2022\033[1;m")
    print("\033[1;32m+ -- -- +=[ This script is under the Unlicense\033[1;m\n")
    print("\033[1;32m[+] Press Enter to continue\033[0m")
    input()
    os.system("clear")
    splash(version)
    menu(version)

def install(version):
    check_dependencies(detect_package_manager())
    i = input('\033[1;33m[?] Do you want to install mrclean ? (y/n) \033[0m')
    if i == 'y' or i == 'Y' or i == 'yes' or i == 'Yes' or i == 'YES':
        os.system('sudo cp resources/mrclean /usr/bin/mrclean')
        os.system('sudo chmod +x /usr/bin/mrclean')
        print('\n\033[1;32m[+] mrclean successfully installed.\033[0m')
        print('\033[1;32m[+] You can now use mrclean.\033[0m\n')
        os.system('sleep 3 ; clear')
        splash(version)
        menu(version)
    else:
        print('\n\033[1;32m[+] mrclean not installed.\033[0m\n')

def menu(version):
    print('\033[1;32m[+] Select an option: \033[0m')
    print('\033[1;32m[1] Install\033[0m')
    print('\033[1;32m[2] Help\033[0m')
    print('\033[1;32m[4] About\033[0m')
    print('\033[1;32m[5] Exit\033[0m\n')

    option = input('\033[1;34mEpi-Dump ➜ \033[0m')
    if option == '1' or option == 'install' or option == 'Install' \
        or option == 'INSTALL' or option == 'i' or option == 'I':
        install(version)
    elif option == '2' or option == 'help' or option == 'Help' or \
        option == 'HELP' or option == 'h' or option == 'H':
        help_func(version)
    elif option == '4' or option == 'about' or option == 'About' or option == 'ABOUT':
        about(version)
    elif option == '5' or option == 'exit' or option == 'quit' or option == 'q' \
        or option == 'Q' or option == 'Exit' or option == 'Quit' or option == 'EXIT' \
        or option == 'QUIT':
        print('\033[1;32m[+] Bye!\033[0m')
        sys.exit(0)
    else:
        print('\n\033[1;31m[!] Invalid option\033[0m\n')
        os.system("sleep 1 ; clear")
        splash(version)
        menu(version)

def main():
    os.system('clear')
    check_internet()
    splash(init_script())
    os.system('sleep 1')
    is_latest_version(init_script())
    if check_internet() == False:
        print('\033[1;31m[!] No internet connection detected.\033[0m')
        sys.exit(1)
    try:
        while True:
            menu(init_script())
    except KeyboardInterrupt:
        print('\n\033[1;32m[+] Ctrl + C pressed, Bye!\033[0m')
        sys.exit(0)

if __name__ == '__main__':
    main()
