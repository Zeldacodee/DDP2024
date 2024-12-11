from Animal import Animal

class Karnivora(Animal) :
    def __init__(self, name, makanan, hidup, berkembang_biak, bernapas) :
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.hidup = hidup
        self.bernapas = bernapas

    def info_karnivora(self) :
        super().info_animal()
        print("hidup \t\t\t\t : ", self.hidup,
              "\nBernafas\t\t\t : ", self.bernapas)
        
Karnivora = Karnivora("macan", "daging", "melahirkan", "darat", "paru-paru")
Karnivora.info_karnivora()