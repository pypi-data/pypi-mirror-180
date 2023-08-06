import paramiko
import sys
from io import StringIO

def ssh_command(host,username,port,privatekey,command):
    print("Bismillah, welcome to command with paramiko-ssh")

    ssh_privatekey = f"""\
    -----BEGIN OPENSSH PRIVATE KEY-----
    {privatekey}
    -----END OPENSSH PRIVATE KEY-----"""

    print(f'HOST = {host}')
    print(f'USERNAME = {username}')
    print(f'PORT = {port}')
    print(f'PRIVATE KEY = {ssh_privatekey}')
    print(f'COMMAND = {command}')


