a=int(input('Mau input berapa nama? '))
l=[]
i=0
for i in range (a):
    nama=input('Masukkan Nama = ' )
    l.append(nama)
l.sort()

r=0
for r in range(len(l)) :
    print(l[r], '(',len(l[r]),'karakter)')
    r+=1
