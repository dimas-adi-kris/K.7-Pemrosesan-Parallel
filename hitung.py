import math

file_r = open("input.txt", "r")
splitted = file_r.read().split(',')
opsi = splitted[0]

sisi = list(map(int, splitted))
if opsi == '1':
    luas = (sisi[1]*sisi[2])/2
    keliling = (sisi[1] + sisi[2] + sisi[3])
elif opsi == '2':
    luas = (sisi[1]*sisi[1])*math.pi
    keliling = (sisi[1]*2)*math.pi
elif opsi == '3':
    luas = (sisi[1]*sisi[2])
    keliling = 2*(sisi[1] + sisi[2])
else:
    luas = 'impossible'
    keliling = ''
print(luas)
print(keliling)
