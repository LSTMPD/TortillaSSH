import paramiko
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", help="Target SSH server you want to connect to")
parser.add_argument("user", help="Username to use")
parser.add_argument("passw", help="Password for the user to authenticate")
args = parser.parse_args()
#print(args.host)

def connect_to_ssh(host, user, passw):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        logger.debug("Connecting to: " + host)
        client.connect(host, 22, user, passw)
        logger.debug("Successfully connected!")
    except socket.error:
        print("Computer is offline or port 22 is closed")
        exit()
    except paramiko.ssh_exception.AuthenticationException:
        print("Wrong Password or Username")
        # TODO: replace exit() and try again with different pass/username
        exit()
    except paramiko.ssh_exception.SSHException:
        # socket is open, but not SSH service responded
        print("No response from SSH server")
        exit()

connect_to_ssh(host, user, passw)

# TODO: Send Commands and get output
