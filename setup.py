import platform
opsys = platform.system()
import os

import subprocess
subprocess.call(['pip', 'install', '-rrequirements.txt'])
if opsys == "Windows":
    os.system("cls")

import configparser
import sys

print("-" * 10)
print(" Do you want to see the welcome banner everytime you run this script? yes/no")
try:
    choice = input("> ")
    while choice not in ['yes', 'no']:
        print("Invalid answer! yes/no")
        choice = input("> ").lower()
except KeyboardInterrupt:
    print("Exiting..")
    exit()

config = configparser.ConfigParser()
config.add_section("Operating System")
config.set("Operating System", "system", opsys)
config.add_section("Settings")
config.set("Settings", "banner", choice)

with open("config.ini", "w") as config_file:
    config.write(config_file)
