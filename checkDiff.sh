#!/bin/bash

scanAndCheck()
{
	if [[ ! -e scans ]]; then
		mkdir scans
	fi
	sudo nmap --open -p- -oX - localhost > scans/tmpscan.xml
	sudo ndiff -v $1 scans/tmpscan.xml > scans/ndiffresults.txt
}
scanAndCheck $1
