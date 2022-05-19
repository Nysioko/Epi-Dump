import sys
import os
import urllib.request


def check_sudo():
    if os.geteuid() != 0:
        print("You need to be root to run this script.")
        sys.exit(1)
    else:
        os.system('clear')

def splash():
    print ("")
    print ("\033[1;34m   ____       _       ___                   \033[0m")
    print ("\033[1;34m  / __/___   (_)____ / _ \ __  __ __ _   ___ \033[0m")
    print ("\033[1;34m / _/ / _ \ / //___// // // /_/ //    \ / _ \ \033[0m")
    print ("\033[1;34m/___// .__//_/     /____/ \____//_/_/_// .__/\033[0m")
    print ("\033[1;34m    /_/                               /_/    \033[0m")
    print ("")
    print ("")
    print (" \033[1;32m+ -- -- +=[ Script by: Nysioko\033[1;m")
    print (" \033[1;32m+ -- -- +=[ Version: 0.1\033[1;m")
    print (" \033[1;32m+ -- -- +=[ Last update: 19 May 2022\033[1;m")
    print ("")
    print ("")
    print ("\033[1;91m[W] This script is under development, please report any bug to @Nysioko\033[0m")
    print ("\033[1;91m[W] This script modify your environment, please be careful with it\033[0m")
    print ("")
    os.system('sleep 1')

def check_internet():
    try:
        urllib.request.urlopen('http://www.google.com')
        return True
    except:
        return False

def detect_package_manager():
    print ('Detecting package manager...')
    print ('Package manager detected: ', end='')
    if os.system('command -v apt') == 0:
        print('\033[1;32mapt\033[0m')
        return 'dnf'
    elif os.system('command -v yum') == 0:
        print('\033[1;32myum\033[0m')
        return 'dnf'
    elif os.system('command -v dnf') == 0:
        print('\033[1;32mdnf\033[0m')
        return 'dnf'
    elif os.system('command -v pacman') == 0:
        print('\033[1;32mpacman\033[0m')
        return 'dnf'
    else:
        print('\033[1;31mUnknown\033[0m')
        return 'unknown'

def check_dependencies():
    print ('Checking dependencies...')
    if detect_package_manager() == 'apt':
        os.system('apt-get update')
        os.system('apt-get install -y wget')
    elif detect_package_manager() == 'yum':
        os.system('yum update')
        os.system('yum install -y wget')
    elif detect_package_manager() == 'pacman':
        os.system('pacman -Sy')
        os.system('pacman -S wget')
    else:
        print('Unknown package manager or no package manager compatible with this script.')
        sys.exit(1)

def main():
    check_sudo()
    splash()
    if check_internet() == False:
        print('\033[1;31m[!] No internet connection detected.\033[0m')
        sys.exit(1)
    detect_package_manager()
    # sys.stdout = open(os.devnull, 'w')
    # check_dependencies()
    # sys.stdout = sys.__stdout__

if __name__ == '__main__':
    main()