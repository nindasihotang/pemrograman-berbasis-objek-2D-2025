class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat


mahasiswa_list = []
for i in range(3):
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    alamat = input("Masukkan alamat: ")
    mhs = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mhs)

for mhs in mahasiswa_list:
    print(f"Nama: {mhs.nama}, NIM: {mhs.nim}, Jurusan: {mhs.jurusan}, Alamat: {mhs.alamat}")