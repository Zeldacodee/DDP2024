from Animal import Animal

class Amphibi(Animal) :
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas) :
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self) :
        super().info_animal()
        print("Jenis air t\t\t\t : ", self.jenis_air,
              "\nBernafas\t\t\t : ", self.bernapas)
        
Amphibi = Amphibi("katak", "serangga", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
Amphibi.info_amphibi()

