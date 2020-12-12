import math

file_r = open("input.txt", "r")
splitted = file_r.read().split(',')
opsi = splitted[0]

sisi = list(map(int, splitted))
if opsi == '1':
    luas = (sisi[1]*sisi[2])/2
    keliling = (sisi[1] + sisi[2] + sisi[3])
    print('Melakukan operasi bangun datar segitiga')
elif opsi == '2':
    luas = (sisi[1]*sisi[1])*math.pi
    keliling = (sisi[1]*2)*math.pi
    print('Melakukan operasi bangun datar lingkaran')
elif opsi == '3':
    luas = (sisi[1]*sisi[2])
    keliling = 2*(sisi[1] + sisi[2])
    print('Melakukan operasi bangun datar persegi')
else:
    luas = 'impossible'
    keliling = ''
print('Luas : ', luas)
print('Keliling : ', keliling)
