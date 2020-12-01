file_r = open("input.txt", "r")
splitted = file_r.read().split(',')
sisi = list(map(int, splitted))
luas = sisi[0] * sisi[1]
print(luas)
