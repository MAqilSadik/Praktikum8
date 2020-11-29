buah = {'apel' :5000, 'jeruk' :8500, 'mangga':7800, 'duku':6500}

namaBuah = str(input('nama buah yang ingin dibeli : '))

a = namaBuah in buah
r = True
if a:

    while (r==True):
        jumlah=float(input('berat buah yg ingin dibeli  =  '))
        harga= buah.get(namaBuah,0)
        Total=jumlah*harga
        print('===================================================')
        print('Total                      = Rp.',Total)
        break

else :
    print('buah tidak tersedia')


















     
