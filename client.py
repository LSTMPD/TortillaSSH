import paramiko
import argparse
import socket
import logging
import coloredlogs
import configparser
import os

# ------------------- Logging ------------------ #
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)
# ---------------------------------------------- #

# ------------------- Config ------------------- #
if 'config.ini':
    config = configparser.ConfigParser()
    config.read('config.ini')
    banner = config.get("Settings", "banner")
    opsys = config.get("Operating System", "system")

else:
    debugger.error("[ERROR] config.ini does not exist! Please run setup.py!")
    exit()
# --------------------------------------------- #

# ------------------- ArgParse ---------------- #
parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Target SSH server you want to connect to")
parser.add_argument("--user", help="Username to use")
parser.add_argument("--passw", help="Password for the user to authenticate")
args = parser.parse_args()
# print(args.host)

if not args.host:
    args.host = input("host: ")
if not args.user:
    args.user = input("username: ")
if not args.passw:
    args.passw = input("password: ")
# ---------------------------------------------- #

# ------------------- Cleaning ----------------- #
def screenclean():
    if opsys == "Windows":
        os.system("cls")

screenclean()
if banner == "yes":
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('TortillaSSH'))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def connect_to_ssh(host, user, passw):
    try:
        logger.debug("Connecting to: " + host)
        client.connect(host, 22, user, passw)
        logger.debug("Successfully connected!")
    except socket.error:
        debugger.error("Computer is offline or port 22 is closed")
        exit()
    except paramiko.ssh_exception.AuthenticationException:
        debugger.error("Wrong Password or Username")
        # TOD replace exit() and try again with different pass/username
        exit()
    except paramiko.ssh_exception.SSHException:
        # socket is open, but not SSH service responded
        debugger.error("No response from SSH server")
        exit()
    except KeyboardInterrupt:
        debugger.error("[KeyboardInterrupt] Exiting..")


connect_to_ssh(args.host, args.user, args.passw)

try:
    while True:
        stdin, stdout, stderr = client.exec_command(input("> "), get_pty=True)
        stdin.close()
        for line in iter(stdout.readline, ""):
            print(line, end="")
except KeyboardInterrupt:
    debugger.eror("[!] Exiting...")
    exit()
