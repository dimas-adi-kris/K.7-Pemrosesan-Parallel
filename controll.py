from paramiko.client import SSHClient, AutoAddPolicy
import sys
import socket
# from getpass import getpass
ssh = '10.1.13.106'
username = 'ldimas'
passhehe = 'root'

ssh2 = '10.1.12.41'
username2 = 'ldimas'
passhehe2 = 'root'

client = []
status = []
client.append(SSHClient())
client.append(SSHClient())

print("Mencoba menghubungkan ke client yang terdaftar")

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
print('''
_________________________________________
|\t{} Status : {}\t|
|\t{} Status : {}\t|
|_______________________________________|
    '''.format(ssh,  status[0],
               ssh2, status[1])
      )


def pilihan():
    print('''
\t AWAL PROGRAM
_______________________________________________
1. Hitung luas dan keliling segitiga
2. Hitung luas dan keliling lingkaran
3. Hitung luas dan keliling persegi


0. Force stop

    ''')
    choice = input('Pilih operasi yang diinginkan : ')
    return choice


def inp_sisi(masukan):
    if masukan == '1':
        print('''
    |\ 
    | \ 
  a |  \ c
    |   \ 
    |____\ 
      b
        ''')
        a = input('a : ')
        b = input('b : ')
        c = input('c : ')
        return [a, b, c]
    elif masukan == '2':
        print('''
    ________
   /        \ 
  /          \ 
 /      __r___\ 
 \            /
  \          /
   \________/
        ''')
        r = input('r : ')
        return [r]
    elif masukan == '3':
        print('''
_________________
|               |
|               |
|               | p
|               |
|_______________|
        l
        ''')
        p = input('p : ')
        l = input('l : ')
        return [p, l]


def write_it(a):
    file1 = open("file_send.txt", "w")
    joined = ','.join(map(str, a))
    file1.write(joined)
    file1.close()


def sendandcount_it(cc):
    print('_______________________________________________')
    print('Mencoba menghubungkan menggunakan sftp')
    try:
        sftp = cc.open_sftp()
        print('Terhubung ke client')
        print('Sedang mengirim...')
        sftp.put('./file_send.txt', './input.txt')
        stdin, stdout, stderr = cc.exec_command('python3 hitung.py')
        baris = stdout.readlines()
        baris_err = stderr.readlines()

        for i in baris_err:
            print(i)
        for i in baris:
            print(i)
    except:
        print("Client ini sedang OFFLINE")
    print('_______________________________________________')


def CloseAllClient(cli):
    for i in cli:
        i.close()


menu = True
while(menu):
    pilih_menu = True
    menu_rumus = []
    while(pilih_menu):
        menu_rumus.clear()
        menu_rumus.append(pilihan())
        if menu_rumus[0] == '1' or menu_rumus[0] == '2' or menu_rumus[0] == '3':
            menu_rumus = menu_rumus + inp_sisi(menu_rumus[0])
            pilih_menu = False
        elif menu_rumus[0] == '0':
            pilih_menu = False
            menu = False
            CloseAllClient(client)
            sys.exit()
        else:
            print('''
_______________________________________________

    MASUKKAN PILIHAN YANG BENAR!!!

_______________________________________________
''')

    print('''
_______________________________________________
Pilih client
    1. {}. Status : {}
    2. {}. Status : {}
    3. Jalankan di kedua client
    '''.format(ssh,  status[0],
               ssh2, status[1])
          )
    input_menu = input('Pilih Client : ')
    if (input_menu == '1'):
        print('Client yang dipilih : '+ssh)
        write_it(menu_rumus)
        sendandcount_it(client[0])
    elif (input_menu == '2'):
        print('Client yang dipilih : '+ssh2)
        write_it(menu_rumus)
        sendandcount_it(client[1])
    elif (input_menu == '3'):
        write_it(menu_rumus)
        print('Client yang dipilih : '+ssh)
        sendandcount_it(client[0])
        print('Client yang dipilih : '+ssh2)
        sendandcount_it(client[1])
    keluar = input(
        "Hentikan Program?\nInput Y/y untuk berhenti\nInput yg lain untuk melanjutkan\nInput : ")
    if (keluar == 'Y' or keluar == 'y'):
        CloseAllClient(client)
        menu = False
