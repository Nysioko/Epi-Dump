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
if grep /etc/os-release | grep -i "debian" | grep -i "ubuntu" > /dev/null ; then
    echo "You are using Debian, the script will continue"
else
    echo "You are not using Debian, the script will stop. Please use Debian and run the script again"
fi