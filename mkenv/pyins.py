#!/env/bin python3

import argparse
from mkenv import Mkenv

"""
    Name: mkenv
    Description: command-line utility that automates my project creation process.
    Usage:
     mkenv --name projectName : creates project setup
     mkenv --activate,        : activate venv
     mkenv --deactivate       : deactivates venv
"""


#Create a directory of the passed name "/name/name
#create a /name/name/name.py and change chmod to u+x
#Create a venv directory on the first level of the project /name/venv
#run python2 -m venv ./venv to create venv instance

parser = argparse.ArgumentParser()
parser.add_argument("--filename", required=True)
parser.add_argument("--setupfile")
args = parser.parse_args()


if bool(args.filename):
    my_project = Mkenv(args.filename)
    my_project.createProject()
