#!/bin/bash
clear
echo "   ____       _       ___                   "
echo "  / __/___   (_)____ / _ \ __ __ __ _   ___ "
echo " / _/ / _ \ / //___// // // // //    \ / _ \ "
echo "/___// .__//_/     /____/ \_,_//_/_/_// .__/"
echo "    /_/                              /_/    "

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run as root\e[0m"
  exit
fi
if curl -s --head  --request GET www.google.com | grep "200 OK" > /dev/null ; then
    echo "You are connected to the internet, the script will continue"
else
    echo "You are not connected to the internet, the script will stop. Please connect to the internet and run the script again"
    exit
fi

echo ""

echo -e "\e[33mChecking your system\e[0m"

#Detect linux distrib
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    OS=SuSE
    VER=$(cat /etc/SuSe-release)
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    OS=RedHat
    VER=$(cat /etc/redhat-release)
elif [ -f /usr/bin/sw_vers ]; then
    OS=MacOS
    VER=$(sw_vers -productVersion)
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
    echo -e "\e[31mYour OS is not supported by this script, please contact the author of this script\e[0m"
fi
sleep 1
echo -e "\e[32mOS: $OS\e[0m"
echo -e "\e[33mVersion: $VER\e[0m"

echo ""
echo -e "\e[32mCompatible distrib detected\e[0m"
sleep 1
echo ""

echo "Please enter your email:" ; read email

if [[ $email = *"@epitech.eu"* ]]; then
    echo -e "\e[32mYour email seems to be valid\e[0m"
else
    echo -e "\e[31mYour need to enter an epitech email\e[0m"
    exit
fi

#Install dependencies for linuxbase.org
if [ "$OS" = "Linux" ]; then
    echo -e "\e[33mInstalling dependencies\e[0m"
    sleep 1
    apt-get update
    apt-get install -y wget curl git
fi

if [ "$OS" = "MacOS" ]; then
    echo -e "\e[33mInstalling dependencies\e[0m"
    echo -e "\e[32mInstalling Homebrew\e[0m"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install wget curl git
fi