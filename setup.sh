#!/bin/bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt install -y python-pip python3-pip
sudo pip3 install nfcpy
sudo pip3 install requests