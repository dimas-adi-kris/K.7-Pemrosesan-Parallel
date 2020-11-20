from paramiko.client import SSHClient,AutoAddPolicy
from getpass import getpass
passhehe = getpass()


client = SSHClient()
# client2 = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
client.connect("10.1.13.106",22,"ldimas",passhehe)

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

















































































