datasayur = ['bayam', 'kangkung', 'wortel', 'selada']
print('Menu:')
print('A. Tambah data Sayur')
print('B. Hapus data Sayur')
print('C. Tampilkan data Sayur')
while True:
    pilihan=input('Masukkan Pilihan Anda(A/B/C)= ')
    if (pilihan=='A'):
        tambah=input('Masukkan sayur yang ingin ditambah = ')
        datasayur.append(tambah)
        print('Data Sayur =', datasayur)
    elif (pilihan=='B'):
        hapus=input('Masukkan sayur yang ingin dihapus = ')
        if hapus in datasayur:
            datasayur.remove(hapus)
            print('Data Sayur =', datasayur)
        else:
            print('Data Sayur Tidak Ditemukan')
    elif (pilihan=='C'):
        print('Data Sayur =', datasayur)
        lagi=input('ingin mengubah(y/n)?')
        if (lagi=='y'):
            continue
        elif (lagi=='n'):
            break
