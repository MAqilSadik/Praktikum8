buah = { 'Apel'  : 5000, 'jeruk' : 8500,'Mangga': 7800,'Duku'  : 6500 }
def reratahargabuah(buah):
    totalharga = 0
    jumlah = 0

    for r,y in buah.items():
        totalharga += y
        jumlah += 1

    ratarata = totalharga/jumlah
    return ratarata

def rerataHargaFruit(buah):
    harga = list(fruit.values())
    rata = sum(harga)/len(harga)
    return rerata

x = reratahargabuah(buah)
print('Rata-rata harga satuan dari seluruh buah yang ada adalah ',x)
