import hitung
import luasbangundatar as bangundatar
from luasbangunruang import kubus
from luasbangunruang import balok
from luasbangunruang import tabung
from luasbangunruang import limas
from luasbangunruang import prisma

# Modul Hitung
print("========== Modul Hitung ==========")
hitung.tambah(10, 10)
hitung.kurang(20, 10)
hitung.kali(10,10)
hitung.bagi(20, 2)
hitung.pangkat(10,2)

print("========== Modul Luas Bangun Datar ==========")
# Modul Luas Bangun Datar
bangundatar.lingkaran(20)
bangundatar.persegi(30)
bangundatar.persegipanjang(50, 25)
bangundatar.segitiga(1/2, 5, 8)
bangundatar.jajargenjang(10, 4)

print("========== Modul Bangun Ruang ==========")
# Modul Bangun Ruang
kubus(10)
balok(12, 5, 10)
tabung(14, 25)
limas(16, 24)
prisma(12, 6, 6)