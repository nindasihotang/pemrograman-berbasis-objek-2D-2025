class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berlari(self):
        print(f"{self.nama} sedang berlari.")
        
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")


orang1 = Manusia("Bapak", 50, "Jambi")
orang2 = Manusia("Mamak", 47, "Riau")
orang3 = Manusia("Roy candra", 27, "Bandung")
orang4 = Manusia("Ridoni", 22, "Riau")
orang5 = Manusia("Ninda artika", 18, "Madura")


orang1.berjalan()
orang2.berlari()
orang3.berjalan()
orang4.berlari()
orang5.berjalan()
