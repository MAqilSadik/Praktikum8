nilaiMhs =[{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 
{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
{'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
{'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
{'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}
]

list = []
for i in range(len(nilaiMhs)):
    daftar = nilaiMhs[i]
    nilaiAkhir = (daftar['mid'] + 2*daftar['uas'])/3
    list.append(nilaiAkhir)

print(max(list))
