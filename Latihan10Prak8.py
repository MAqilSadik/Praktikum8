buah = {'apel': 5000,'jeruk' : 8500,'mangga' : 7800,'duku' : 6500}

sum = 0
lagi = 'y'
while lagi == 'y':
    nama_buah = str(input('Nama buah yang ingin dibeli  :  '))
    if nama_buah in buah :
        for x,y in buah.items() :
            if(x == nama_buah):
                berat = float(input('Berat buah yang ingin dibeli : '))
                harga = berat * y
    else:
        print('Maaf, buah yang diminta tidak tersedia')
    sum += harga
    lagi = str(input('Beli buah yang lain (y/n)? '))
    
print('---------------------------------------------------------')
print('Total harga                  : Rp.'+ str(sum))
