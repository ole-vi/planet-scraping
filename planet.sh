#!/bin/bash

# Check if selenium is intalled and install if not 
if python3 -c 'import selenium'; then
	echo 'selenium is already installed'
else
	pip3 install -U selenium
fi

git clone https://github.com/treehouses/treehouses.github.io.git
zip -r treehouses.zip treehouses.github.io

# Export private login info
chmod u+x config.sh
source config.sh

python3 planet.py


