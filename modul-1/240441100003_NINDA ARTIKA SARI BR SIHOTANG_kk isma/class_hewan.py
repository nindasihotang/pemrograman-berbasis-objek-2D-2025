class Hewan:
    def __init__(self, nama, umur, jenis):
        self.nama = nama
        self.umur = umur  
        self.jenis = jenis

    def bergerak(self):
        print(f"{self.nama} yang merupakan {self.jenis} sedang bergerak.")

    def bersuara(self):
        print(f"{self.nama} yang merupakan {self.jenis} bersuara.")


hewan_list = [
    Hewan("Gajah", 4, "Herbivora"),
    Hewan("Harimau", 3, "Carnivora"),
    Hewan("Hamster", 2, "Omnivora"),
    Hewan("Lebah", 1, "Insektivora")
]

#looping untuk menampilkan data hewan
for hewan in hewan_list:
    hewan.bergerak()
    hewan.bersuara()