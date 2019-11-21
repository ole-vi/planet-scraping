#!/bin/bash

if python3 -c 'import selenium'; then
	echo 'selenium installed'
else
	pip3 install -U selenium
fi

#pip3 install -U selenium

git clone https://github.com/treehouses/treehouses.github.io.git
zip -r treehouses.zip treehouses.github.io

# python3 pythonscrape.py

#curl -T treehouses.github.io http://localhost:5984/_utils/#database/resources/_all_docs

#curl -X PUT -T /Users/XavierElon/Library/Mobile\ Documents/com~apple~CloudDocs/hacking/python/treehouses.github.io http://localhost:5984/resources/treehouses -u xavierelon:toor
