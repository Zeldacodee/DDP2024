class Gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):
        print()
        print(f"Ada gempa baru nih di {self.lokasi}")
        print (f"skala dari gempa ini adalah {self.skala}")
        if self.skala < 2:
            print('Dampak ga berasa')
        elif self.skala >= 2 and self.skala <= 4:
            print ('dampak gempa bangunan retak - retak')
        elif self.skala > 4 and self.skala <= 6:
            print('dampak gempa bangunan roboh')
        elif self.skala > 6 :
            print('dampak bangunan roboh dan potensi tsunamai')
        else :
            print('sistem tidak dapat membaca')

#Gempa().skala = 2
#Gempa().dampak()

Gempa1 = Gempa(5,"jawa barat")
Gempa1.dampak()


        
