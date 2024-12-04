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
