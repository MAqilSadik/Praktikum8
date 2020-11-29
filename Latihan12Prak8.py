buah = { 'apel'  : 5000,
         'jeruk' : 8500,
         'mangga' : 7800,
         'duku'  : 6500 }

def printDataBuah(databaseBuah):
    print("Data Buah")
    for i, j in databaseBuah.items():
        print("- {0} (Harga Rp{1} / kg)".format(i,j))
    print()

def checkOut(databaseBuah,namaBuah,banyakKilo):
    hargaBuah = databaseBuah.get(namaBuah)
    totalHarga = hargaBuah * banyakKilo
    return totalHarga

while True:
    print("Menu :\nA. Tambah data buah\nB. Beli buah\nC. Hapus data buah\nD. Selesai")
    opsi = None
    
    while opsi not in("A","B","C","D"):
        opsi = str(input("Pilihan Menu: "))
        
        if(opsi == "A"):
            printDataBuah(buah)
            namaBuahTambahan = str(input("Nama buah yang ditambahkan: "))
            if namaBuahTambahan in buah.keys():
                print("Buah telah terdaftar dalam database")
            else:
                while True:
                    try:
                        hargaBuahTambahan = int(input("Harga buah (dalam angka): "))
                    except ValueError:
                        print("Masukkan kembali dalam angka")
                        continue
                    else:
                        break
                    
                buah[namaBuahTambahan] = hargaBuahTambahan
                print("{0} dengan harga {1} telah ditambahkan dalam database".format(namaBuahTambahan,hargaBuahTambahan))
                print("")
                printDataBuah(buah)
                
        elif(opsi == "B"):
            printDataBuah(buah)
            totalHarga = 0
            selesai = False
            while not(selesai):
                while True:
                    namaBuah= str(input("Nama buah yang dibeli              : "))
                    if(not(namaBuah in buah.keys())):
                        print("Nama buah tidak ditemukan")
                        continue
                    else:
                        break
                while True:
                    try:
                        kiloan = float(input("Berapa kg (apabila desimal gunakan titik)   : "))                   
                    except ValueError:
                        print("Masukkan kembali dalam angka")
                        continue
                    else:
                        break
                totalHarga = totalHarga + checkOut(buah,namaBuah,kiloan)
                opsi = None
                while opsi not in("y","n"):
                    opsi = str(input("Beli lagi (y/n)?"))
                    if(opsi == "y"):
                        selesai = False
                        print()
                    elif(opsi == "n"):
                        selesai = True
                    else:
                        print("Masukkan pilihan (y/n)")
                print("------------------------------------------------")
                print("Total harga                              : {0}".format(totalHarga))
                
        elif(opsi == "C"):
            printDataBuah(buah)
            namaBuahHapus = str(input("Nama buah yang dihapus: "))
            if namaBuahHapus in buah.keys():
                del buah[namaBuahHapus]
                print("Nama fruit {0} telah terhapus dalam database".format(namaBuahHapus))
                print()
                printDataBuah(buah)
            else:
                print("Nama buah tidak ditemukan")
                
        elif(opsi == "D"):
            break
            
        else:
            print("Mohon masukkan pilihan yang tersedia")
