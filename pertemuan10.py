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


    # Membuat Modul Untuk Menghitung Luas Bangun Ruang

def kubus(rusuk):
    hasil = rusuk**3
    print(f'Hasil dari luas volume kubus {rusuk} = {hasil}')

def balok(panjang, lebar, tinggi):
    dua = 2
    hasil = dua * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print(f'Hasil dari luas balok {dua} * ({panjang} * {lebar} + {panjang} * {tinggi} + {lebar} * {tinggi}) = {hasil}')

def tabung(jari2, tinggi):
    phi = 22/7
    dua = 2
    hasil = dua * phi * jari2 * (jari2 + tinggi)
    print(f'Hasil dari luas tabung {dua} * {phi} * {jari2} * ({jari2 + tinggi}) = {hasil}')

def limas(luas_alas, jumlah_luas_sisi_tegak):
    hasil = luas_alas + jumlah_luas_sisi_tegak
    print(f'Hasil dari luas permukaan limas {luas_alas} + {jumlah_luas_sisi_tegak} = {hasil}')

def prisma(keliling_alas_prisma, tinggi, luas_alas_prisma):
    dua = 2
    hasil = (keliling_alas_prisma * tinggi) + (dua * luas_alas_prisma)
    print(f'Hasil dari luas permukaan prisma ({keliling_alas_prisma} * {tinggi}) + ({dua} * {luas_alas_prisma}) = {hasil}')



    # Membuat Modul Hitung
import math

def tambah(bilangan1, bilangan2):
    hasil = bilangan1 +bilangan2
    print(f'Hasil dari penjumlahan {bilangan1} + {bilangan2} = {hasil}')

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print(f'Hasil dari pengurangan {bil1} - {bil2} = {hasil}')

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print(f'Hasil dari perkalian {bil1} x {bil2} = {hasil}')

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print(f'Hasil dari pembagian {bil1} / {bil2} = {hasil}')

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print(f'Hasil dari pemangkatan {bil1} ^ {bil2} = {hasil}')