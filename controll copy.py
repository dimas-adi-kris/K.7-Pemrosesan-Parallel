from paramiko.client import SSHClient, AutoAddPolicy
# import paramiko.socket.gaierror as gai
import sys
import socket
from getpass import getpass
ssh = '10.1.13.106'
passhehe = 'root'
username = 'ldimas'

ssh2 = '10.10.10.10'
passhehe2 = 'root'
username2 = 'ldimas'

client = []
client.append(SSHClient())
client.append(SSHClient())

print(client[0])
for i in client:
    i.close()
