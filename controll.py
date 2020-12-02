from paramiko.client import SSHClient, AutoAddPolicy
import sys
import socket
# from getpass import getpass
ssh = '10.1.13.106'
passhehe = 'root'
username = 'ldimas'

ssh2 = '10.1.12.41'
passhehe2 = 'root'
username2 = 'ldimas'

client = []
status = []
client.append(SSHClient())
client.append(SSHClient())


client[0].set_missing_host_key_policy(AutoAddPolicy())
try:
    client[0].connect(ssh, 22, username, passhehe, timeout=5)
    status.append('ONLINE')
except (socket.gaierror, socket.timeout):
    status.append('OFFLINE')

client[1].set_missing_host_key_policy(AutoAddPolicy())
try:
    client[1].connect(ssh2, 22, username2, passhehe2, timeout=5)
    status.append('ONLINE')
except (socket.gaierror, socket.timeout):
    status.append('OFFLINE')


def write_it(a):
    file1 = open("file_send.txt", "w")
    joined = ','.join(map(str, a))
    file1.write(joined)
    file1.close()


def sendandcount_it(cc):
    print('_______________________')
    try:
        sftp = cc.open_sftp()
        sftp.put('./file_send.txt', './input.txt')
        stdin, stdout, stderr = cc.exec_command('python3 luaspersegi.py')
        baris = stdout.readlines()
        baris_err = stderr.readlines()

        for i in baris_err:
            print(i)
        for i in baris:
            print(i)
    except:
        print("Client ini sedang OFFLINE")


menu = True
while(menu):
    a = ['0', '0']
    a[0] = input("Masukkan panjang :")
    a[1] = input("Masukkan lebar :")
    print('''Pilih client
    1. {}. Status : {}
    2. {}. Status : {}
    3. Jalankan di kedua client
    '''.format(ssh,  status[0],
               ssh2, status[1])
          )
    input_menu = input('Pilih Client : ')
    if (input_menu == '1'):
        write_it(a)
        sendandcount_it(client[0])
    elif (input_menu == '2'):
        write_it(a)
        sendandcount_it(client[1])
    elif (input_menu == '3'):
        write_it(a)
        sendandcount_it(client[0])
        sendandcount_it(client[1])
    keluar = input("Hentikan Program?(Y/y)")
    if (keluar == 'Y' or keluar == 'y'):
        for i in client:
            i.close()
        sys.exit()
