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