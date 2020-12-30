#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

apt install acl -y
useradd -M apiuser
usermod -L apiuser
setfacl -m u:apiuser:rwx /apps/logs/weather_api
