#Buatlah list a = [1, 5, 6, 3, 6, 9, 11, 20, 12] dan b = [7, 4, 5, 6, 7, 1, 12, 5, 9
#nomor 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print('List a :\n', a)
print('List b :\n', b)
print("===============================")

#Sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b
#nomor 2
a.insert(3,10)
b.insert(2,15)
print('List a setelah disisipkan nilai 10 ke indeks 3 dari a :\n',a)
print('List b setelah disisipkan nilai 15 ke indeks 2 dari b :\n',b)
print("===============================")

#Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b
#nomor 3
a.append(4)
b.append(8)
print('setelah disisipkan nilai 4 ke indeks terakhir dari a:\n',a)
print('setelah disisipkan nilai 8 ke indeks terakhir dari b:\n',b)
print("===============================")

#Kemudian lakukan sorting secara ascending pada list a dan b
#nomor 4
a.sort()
b.sort()
print('List a setelah sorting secara ascending:\n',a)
print('List b setelah sorting secara ascending:\n',b)
print("===============================")

#Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
#nomor 5
c=a[:8]
d=b[2:10]
print('List c yang elemennya merupakan sublist dari a(mulai dari indeks 0-7):\n',c)
print('List d yang elemennya merupakan sublist dari b(mulai dari indeks 2-9):\n',d)
print("===============================")

#Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.e = [c0+d0, c1+d1, c2+d2, ...] Petunjuk: gunakan looping for
#nomor 6
e=[]
for i in range(len(d)):
    e += [c[i]+d[i]]
print('List e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d:\n',e)

#Ubahlah list e ke dalam tuple
#nomor 7
e=tuple(e)
print('List e yang dijadikan tuple:\n',e)
print("===============================")

#Carilah nilai min, maks, dan jumlahan seluruh elemen dari e
#nomor 8
min=min(e)
max=max(e)
sum=sum(e)
print('Nilai Min dari seluruh elemen e:\n',min)
print('Nilai Max dari seluruh elemen e:\n',max)
print('Sum dari seluruh elemen e:\n',sum)
print("===============================")

#Buatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”
#nomor 9
myString="python adalah bahasa pemrograman yang menyenangkan"
print('myString:\n',myString)
print("===============================")

#Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut
#nomor 10
myStringSet=set(myString)
print('Karakter huruf yang menyusun myString:\n',myStringSet)
print("===============================")

#Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list.
#nomor 11
myStringSetList = list(myStringSet)
print('List myString\n',myStringSetList)
myStringSetList.sort()
print('List alfabet himpunan myString:\n',myStringSetList)
