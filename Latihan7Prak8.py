daftarbuah = {
    'Apel'  : 5000,
    'Jeruk' : 8500,
    'Mangga': 7800,
    'Duku'  : 6500
}

def mostExpensive(dictionary) :
    
    key = list(dictionary.keys())
    values = tuple(dictionary.values())
    hargaExpensive = max(values)
    indexHargaExpensive = values.index(hargaExpensive)
    print(key[indexHargaExpensive])
    
print('Harga buah yang paling mahal adalah :')
mostExpensive(daftarbuah)
