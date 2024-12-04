# Membuat Modul Untuk Menghitung Luas Bangun Datar

def lingkaran(jari2):
    phi = 3.14
    hitung = phi*jari2**2
    print(f'Hasil dari luas lingkaran {jari2} = {hitung}')

def persegi(sisi):
    hitung = sisi * sisi
    print(f'Hasil dari luas persegi {sisi} = {hitung}')

def persegipanjang(panjang, lebar):
    hitung = panjang * lebar
    print(f'Hasil dari luas persegi panjang {panjang} * {lebar} = {hitung}')

def segitiga(setengah, alas, tinggi):
    hitung = setengah * alas * tinggi
    print(f'Hasil dari luas segitiga {setengah} * {alas} * {tinggi} = {hitung}')

def jajargenjang(alas, tinggi):
    hitung = alas * tinggi
    print(f'Hasil dari luas jajargenjang {alas} * {tinggi} = {hitung}')
