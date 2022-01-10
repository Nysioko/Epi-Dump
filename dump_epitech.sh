#!/bin/bash
clear
echo "#########################################################################"
echo "####################### DUMP EPITECH DEBIAN #############################"
echo "#########################################################################"
if [ "$EUID" -ne 0 ]
  then echo "The script must be run as root. Please use sudo and run the script again."
  exit
fi
if curl -s --head  --request GET www.google.com | grep "200 OK" > /dev/null ; then
    echo "You are connected to the internet, the script will continue"
else
    echo "You are not connected to the internet, the script will stop. Please connect to the internet and run the script again"
fi
if grep -q "debian" /etc/os-release | grep -q "ubuntu" /etc/os-release; then
    echo "You are using Debian, the script will continue"
else
    echo "You are not using Debian, the script will stop. Please use Debian and run the script again"
fi

echo "Yeah, you are ready to go, let's start the script"

read -p "Please enter your {Epitech.} login: " login

echo "Adding PPAs"

echo "The script will now install the dependencies; this may take a while, please be patient..."

echo "Changing directory to /tmp and downloading the dependencies"
cd /tmp

## Update the system
apt-get update
echo "done."

apt-get upgrade
echo "done."

## Install the dependencies

apt-get install -y wget
echo "done."

apt-get install -y curl
echo "done."

apt-get install -y git
echo "done."

apt-get install -y vim
echo "done."

apt-get install emacs-nox
echo "done."

apt-get install -y python-pip
echo "done."

apt-get install -y python
echo "done."

apt-get install -y python-setuptools
echo "done."

apt-get install -y python-virtualenv
echo "done."

apt-get install -y valgrind
echo "done."

apt-get install -y libxml2-dev
echo "done."

apt-get install -y libxslt-dev
echo "done."

apt-get install -y libjpeg-dev
echo "done."

apt-get install -y libpng-dev
echo "done."

apt-get install -y libfreetype6-dev
echo "done."

apt-get install -y libssl-dev
echo "done."

apt-get install -y libffi-dev
echo "done."

apt-get install -y libxmlsec1-dev
echo "done."

apt-get install -y libxmlsec1-openssl
echo "done."

apt-get install -y build-essential
echo "done."

apt-get install -y libpq-dev
echo "done."

apt-get install -y libpq5
echo "done."

apt-get install -y lncurses-dev
echo "done."

apt-get install -y libncurses5-dev
echo "done."

apt-get install -y libncursesw5-dev
echo "done."

apt-get install -y ghc
echo "done."

if read -t 5 -p "Do you want generate a SSH key for GitHub? (y/n) " answer; then
    if [ "$answer" = "y" ]; then
        echo "Generating SSH key for GitHub..."
        ssh-keygen -t rsa -b 4096 -C $login
        echo "done."
    else
        echo "Ok, we won't generate a SSH key for GitHub"
    fi
else
    echo "You chose not to install the requirements"
fi