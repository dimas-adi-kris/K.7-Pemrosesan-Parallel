from paramiko.client import SSHClient,AutoAddPolicy
# import paramiko.socket.gaierror as gai
import sys
import socket
from getpass import getpass
ssh = input("Ssh: ")
passhehe = getpass()
username = input("Username: ")

client = SSHClient()
# client2 = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
try:
  client.connect(ssh,22,username,passhehe)
  status = 'ONLINE'
except socket.gaierror:
  status = 'OFFLINE'
# client.connect(ssh,22,username,passhehe)

menu = True
while(menu):
  print('Status perangkat : {} ({})'.format(ssh,status))
  print('Menu \n 1. print do something\n 2. exit')
  input_menu = input('Masukkan pilihan aksi : ')
  if (input_menu == '1'):
    print('Do Something')
  elif (input_menu == '0'):
    print('exit')
    sys.exit()
    # menu = False
    
sys.exit()
print('Status perangkat : {} ({})'.format(ssh,status))
# client2.set_missing_host_key_policy(AutoAddPolicy())
# client2.connect("10.1.14.144",22,"dimasdi",passhehe)

while(True):  
  stdin,stdout,stderr = client.exec_command('python3 tugasK7U.py')
  # stdin2,stdout2,stderr2 = client2.exec_command('python3 tugasK7U.py')
  lines = stdout.readlines()
  lines_err = stderr.readlines()
  # lines2 = stdout2.readlines()
  # lines_err2 = stderr2.readlines()

  for i in lines_err:
    print(i)
  for i in lines:
    print(i)

  # for i2 in lines_err2:
  #   print(i2)
  # for i2 in lines2:
  #   print(i2)

client.close()
# client2.close()

















































































