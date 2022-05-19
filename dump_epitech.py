import sys
import os
import urllib.request
import contextlib

def check_sudo():
    if os.geteuid() != 0:
        print("You need to be root to run this script.")
        sys.exit(1)
    else:
        os.system('clear')

def splash(version):
    print("")
    print("\033[1;34m   ____       _       ___                   \033[0m")
    print("\033[1;34m  / __/___  (_)____ / _ \ __  __ __ _   ___ \033[0m")
    print("\033[1;34m / _/ / _ \ / //___// // // /_/ //    \ / _ \ \033[0m")
    print("\033[1;34m/___// .__//_/     /____/ \____//_/_/_// .__/\033[0m")
    print("\033[1;34m    /_/                               /_/    \033[0m\n\n")
    print(" \033[1;32m+ -- -- +=[ Script by: Nysioko\033[1;m")
    print(" \033[1;32m+ -- -- +=[ Version: " + version +"\033[1;m")
    print(" \033[1;32m+ -- -- +=[ Last update: 19 May 2022\033[1;m\n\n")
    print("\033[1;91m[W] This script is under development, please report any bug to @Nysioko\033[0m")
    print("\033[1;91m[W] This script modify your environment, please be careful with it\033[0m\n")
    os.system('sleep 1')

def check_internet():
    try:
        urllib.request.urlopen('http://www.google.com')
        return True
    except:
        return False

def is_latest_version(version):
    print('Checking script version...')
    os.system("wget -O /tmp/.version https://raw.githubusercontent.com/Nysioko/EpiDump/main/.version > /dev/null 2>&1")
    online_version = open("/tmp/.version").read()
    if online_version == version:
        print('\033[1;32m[+] You are using the latest version of the script.\033[0m\n')
    else:
        if(version > online_version):
            print('\033[1;31m[!] This version is too highest in comparison to the online version.\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
        elif(version.isnumeric() == False):
            print('\033[1;31m[!] This version is not a number.\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')
        else:
            print('\033[1;31m[!] You are not using the latest version of the script.\033[0m')
            print('\033[1;31m[!] Actual version: \033[1;32m' + version + '\033[0m')
            print('\033[1;31m[!] Latest version: \033[1;32m' + open("/tmp/.version").read() + '\033[0m')
            print('\033[1;33m[!] Pulling the latest version...\033[0m\n')


def detect_package_manager():
    print('Detecting package manager...')
    print('Package manager detected: ', end='')
    if os.system('command -v apt > /dev/null 2>&1') == 0:
        print('\033[1;32mapt\033[0m\n')
        return 'apt'
    elif os.system('command -v yum > /dev/null 2>&1') == 0:
        print('\033[1;32myum\033[0m\n')
        return 'yum'
    elif os.system('command -v dnf > /dev/null 2>&1') == 0:
        print('\033[1;32mdnf\033[0m\n')
        return 'dnf'
    elif os.system('command -v pacman > /dev/null 2>&1') == 0:
        print('\033[1;32mpacman\033[0m\n')
        return 'pacman'
    else:
        print('\033[1;31mUnknown\033[0m')
        return 'unknown'

def check_dependencies():
    print('Checking dependencies...')
    if detect_package_manager() == 'apt':
        os.system('apt-get update > /dev/null 2>&1')
        os.system('apt-get install -y wget > /dev/null 2>&1')
    elif detect_package_manager() == 'yum':
        os.system('yum update > /dev/null 2>&1')
        os.system('yum install -y wget > /dev/null 2>&1')
    elif detect_package_manager() == 'pacman':
        os.system('pacman -Sy > /dev/null 2>&1')
        os.system('pacman -S wget > /dev/null 2>&1')
    else:
        print('Unknown package manager or no package manager compatible with this script.')
        sys.exit(1)

def main():
    if os.path.isfile('.version') == False:
        print('\033[1;31m[!] No version file detected.\033[0m')
        print('\033[1;31m[!] Please verify that you are in the right directory or the repository is correctly cloned.\033[0m')
        sys.exit(1)
    else:
        version = open('.version').read()
    check_sudo()
    splash(version)
    is_latest_version(version)
    if check_internet() == False:
        print('\033[1;31m[!] No internet connection detected.\033[0m')
        sys.exit(1)
    detect_package_manager()
    #check_dependencies()

if __name__ == '__main__':
    main()