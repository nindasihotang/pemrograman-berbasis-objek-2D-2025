class Mahasiswa:
    total_mahasiswa = 0  

    def __init__(self, nama, nim, prodi):
        if not self.validasi_nim(nim):
            print(f"peringatan: NIM '{nim}' tidak valid.")

        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.total_mahasiswa += 1  
  
    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("2") and len(nim) == 10

    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)

    def tampilkan_biodata(self):
        matkul_list = ', '.join([mk.nama for mk in self.mata_kuliah])
        return f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}, Mata Kuliah: {matkul_list}"

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa


class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not self.validasi_sks(sks):
            print(f"Peringatan: SKS '{sks}' tidak valid untuk mata kuliah '{nama}'.")
            
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]


class Kampus:
    def __init__(self, nama, alamat):
        if not self.validasi_nama_kampus(nama):
            print(f"Peringatan: Nama kampus '{nama}' tidak valid.")
            
        self.nama = nama
        self.alamat = alamat
        self.total_mahasiswa = Mahasiswa.jumlah_mahasiswa() 

    @staticmethod
    def validasi_nama_kampus(nama):
        return nama.replace(" ", "").isalpha()


    def tampilkan_info_kampus(self):
        return f"Nama Kampus: {self.nama}, Alamat: {self.alamat}, Total Mahasiswa: {self.total_mahasiswa}"


# objek mahasiswa
mahasiswa1 = Mahasiswa("ninda", "2304411021", "sistem Informasi")
mahasiswa2 = Mahasiswa("monica", "2304411052", "sistem Informasi")
mahasiswa3 = Mahasiswa("anna", "2304411073", "sistem Informasi")
mahasiswa4 = Mahasiswa("rosa", "2304411014", "sistem Informasi")
mahasiswa5 = Mahasiswa("regita", "2304411085", "sistem Informasi")
mahasiswa6 = Mahasiswa("sinta", "2304411046", "sistem Informasi")
mahasiswa7 = Mahasiswa("fira", "2304411080", "sistem Informasi")

# objek MataKuliah 
matkul1 = MataKuliah("SI112", "Algoritma Pemrograman", 3)
matkul2 = MataKuliah("SI115", "Statistik", 3)
matkul3 = MataKuliah("SI116", "Logika Engineering", 2)
matkul4 = MataKuliah("SI113", "Keterampilan Interpersonal", 3)
matkul5 = MataKuliah("SI111", "PTIK", 3)
matkul6 = MataKuliah("SI108", "Pancasila", 2)
matkul7 = MataKuliah("SI114", "Menajemen & Organisasi", 3)
matkul8 = MataKuliah("SI117", "Agama", 2)

# Menambahkan mata kuliah ke mahasiswa
mahasiswa1.tambah_mata_kuliah(matkul1)
mahasiswa1.tambah_mata_kuliah(matkul2)
mahasiswa1.tambah_mata_kuliah(matkul3)
mahasiswa1.tambah_mata_kuliah(matkul4)
mahasiswa1.tambah_mata_kuliah(matkul5)

mahasiswa2.tambah_mata_kuliah(matkul4)
mahasiswa2.tambah_mata_kuliah(matkul3)
mahasiswa2.tambah_mata_kuliah(matkul2)
mahasiswa2.tambah_mata_kuliah(matkul1)

mahasiswa3.tambah_mata_kuliah(matkul8)
mahasiswa3.tambah_mata_kuliah(matkul7)
mahasiswa3.tambah_mata_kuliah(matkul6)
mahasiswa3.tambah_mata_kuliah(matkul5)

mahasiswa4.tambah_mata_kuliah(matkul5)
mahasiswa4.tambah_mata_kuliah(matkul6)
mahasiswa4.tambah_mata_kuliah(matkul7)
mahasiswa4.tambah_mata_kuliah(matkul8)

mahasiswa5.tambah_mata_kuliah(matkul1)
mahasiswa5.tambah_mata_kuliah(matkul2)
mahasiswa5.tambah_mata_kuliah(matkul7)
mahasiswa5.tambah_mata_kuliah(matkul8)

mahasiswa6.tambah_mata_kuliah(matkul3)
mahasiswa6.tambah_mata_kuliah(matkul4)
mahasiswa6.tambah_mata_kuliah(matkul5)
mahasiswa6.tambah_mata_kuliah(matkul6)

mahasiswa7.tambah_mata_kuliah(matkul3)
mahasiswa7.tambah_mata_kuliah(matkul4)
mahasiswa7.tambah_mata_kuliah(matkul1)

# Menampilkan biodata mahasiswa
daftar_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5, mahasiswa6, mahasiswa7]
print("===Data Mahasiswa====")
for mhs in daftar_mahasiswa:
    print(mhs.tampilkan_biodata())

# Membuat objek kampus
kampus = Kampus("Universitas Trunojoyo Madura97", "Jl. Raya Telang,")
print("===Info Kampus===")
print(kampus.tampilkan_info_kampus())
