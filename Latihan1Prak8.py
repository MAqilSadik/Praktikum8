n = int(input('Tentukan jumlah bilangan bulat yang ingin dimasukkan : '))
bil = []
for i in range(n):
    n = int(input('Masukkan bilangan bulat : '))
    bil.append(n)
bil.sort()
bil.reverse()
print(bil)
