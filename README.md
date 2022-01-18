# Open port scan system with notifications

This utility was made to allow automation of monitoring opened ports on local machine, using a model *.xml* scan file.

# Installation

Installation instructions for port scan system are provided here.

## Dependency Setup
Install [argparse](https://pypi.org/project/argparse/)>=1.4.0, [plyer](https://pypi.org/project/plyer/)>=2.0.0
```
pip install argparse
pip install plyer
```

Install the [nmap](https://nmap.org/), [ndiff](https://nmap.org/book/ndiff-man.html) tools. For example:
```
sudo apt-get update
sudo apt-get install nmap
sudo apt-get install ndiff
```

## Model File Preparation
Using nmap tool perform a scan of host with only wanted ports open and save it into *.xml* file and place it with in *scans* directory:
```
nmap --open -p- -oX - <host> > testscan.xml
```

## Compare and notification tool usage
```
python3 scanner.py [Options]

-c, --continuous
    optional, for continuous scan performing and checking for differences between model and current scans.
-s, --sleep
    optional, how long in seconds to wait after the notification has disappeared for performing next scan and comparison. default 60
-t, --time
    optional, how long in seconds the notifications should be visible. default 20
-p, --path
    optional, the path to model xml file.default scans/testscan.xml
```

## Results of comparison
A list of unwanted open ports is going to appear in the same directory as *scanner.py* file
