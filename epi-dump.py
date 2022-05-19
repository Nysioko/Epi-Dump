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
                print('\033[1;31m[!] Please verify that you are in the right directory or the repository is correctly cloned.\033[0m')
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
    print("\033[1;32m+ -- -- +=[ Version: " + version +"\033[1;m")
    print("\033[1;32m+ -- -- +=[ Last update: 19 May 2022\033[1;m")
    print("\033[1;32m+ -- -- +=[ This script is under the Unlicense\033[1;m\n\n")
    print("\033[1;91m[W] This script is under development, please report any bug to @Nysioko\033[0m")
    print("\033[1;91m[W] This script modify your environment, please be careful with it\033[0m\n")
    os.system('sleep 1')

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

def is_latest_version(version):
    print('Checking script version...')
    os.system("wget -O /tmp/.version https://raw.githubusercontent.com/Nysioko/EpiDump/main/.version > /dev/null 2>&1")
    if os.path.isfile('/tmp/.version') == False:
        print('\033[1;31m[!] Impossible to check version, please try again later\033[0m')
        print('\033[1;31m[!] If the problem persist, please report it to @Nysioko\033[0m')
        sys.exit(1)
    online_version = open("/tmp/.version").read()

    if online_version == version:
        print('\033[1;32m[+] You are using the latest version of the script.\033[0m\n')
        os.system('rm /tmp/.version')
    else:
        if (version > online_version):
            print('\033[1;31m[!] This version is too highest in comparison to the online version.\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
            os.system('rm /tmp/.version')
            #restart_script()
        else:
            print('\033[1;31m[!] You are not using the latest version of the script.\033[0m')
            print('\033[1;31m[!] Actual version: \033[1;32m' + version + '\033[0m')
            print('\033[1;31m[!] Latest version: \033[1;32m' + open("/tmp/.version").read() + '\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
            os.system('rm /tmp/.version')
            #restart_script()

def detect_package_manager():
    print('Detecting package manager...')
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

def check_dependencies(package_manager):
    dependancies = ['wget', 'curl', 'gcc', 'g++']
    print('Checking dependencies...')

    for i in dependancies:
        #os.system(package_manager + '-y' + i + ' > /dev/null 2>&1')
        if os.system('command -v ' + i + ' > /dev/null 2>&1') == 0:
            print('\033[1;32m' + i + '\033[0m', end='')
            if i != dependancies[-1]:
                print('\033[1;32m, \033[0m', end='')
        else:
            print('\033[1;31m' + i + '\033[0m')
            print('\033[1;31m[!] Please install ' + i + ' to continue\033[0m')
            sys.exit(1)
    print('\n')

def main():
    os.system('clear')
    splash(init_script())
    is_latest_version(init_script())
    if check_internet() == False:
        print('\033[1;31m[!] No internet connection detected.\033[0m')
        sys.exit(1)
    check_dependencies(detect_package_manager())

if __name__ == '__main__':
    main()