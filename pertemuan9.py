#buatlah 
print('## nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32 #mengkonversi suhu dari celcius ke fahrenheit
    return fahrenheit #mengembalikan nilai fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
# Cetak 100 celcius ke 32 fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
# cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)
print ('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 #menentukan bilangan ganjil atau genap
    return hitung # mengembalikan nilai hitung 

angka1 = 4 # mendefenisi bilangan 
hasil1 = genap_ganjil(angka1)   
print (f"Bilangan {angka1} bernilai {hasil1}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai (hasil2)")


print ('## Nomor 3 ##')

def cek_kelulusan(nilai):
    if nilai > 60 :
        return 'lulus'
    else:
        return 'tidak lulus'

nilai_kamu1 = 80 # mendefinisi nilai
status1 = cek_kelulusan(nilai_kamu1) # memanggil fungsi dan parameter
print(f"Nilai: {nilai_kamu1}, status: {status1}")

nilai_kamu2 = 60 # mendefinisi nilai
status2 = cek_kelulusan(nilai_kamu2) # memanggil fungsi dan parameter
print(f"Nilai: {nilai_kamu2}, status: {status2}")
 
print('## Nomor 4 ##')
def bilangan_ganjil(number):
    for a in range(1, number, 2):
        print(a, end=" ")
        
bilangan_ganjil(20)








