# Buat class Mahasiswa.
# Class memiliki atribut: nama, nim, nilai.
# Buat method tampilkan_info() untuk mencetak info mahasiswa.
# Buat 2 object mahasiswa dan tampilkan datanya.

class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self.nim = nim
    self.nilai = nilai

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Nim: {self.nim}")
    print(f"Nilai: {self.nilai}")

mhs1 = Mahasiswa("Andi", "12345", 85)
mhs1.tampilkan_info()

mhs2 = Mahasiswa("Budi", "67890", 90)
mhs2.tampilkan_info()

# Modifikasi class Mahasiswa:
# Tambahkan method nilai_huruf() yang mengubah nilai angka menjadi huruf berdasarkan kriteria:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# < 60 : E
# Tampilkan nilai huruf di tampilkan_info()

class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self.nim = nim
    self.nilai = nilai
  
  def nilai_huruf(self):
    if self.nilai >= 90:
        return "A"
    elif self.nilai >= 80:
        return "B"
    elif self.nilai >= 70:
        return "C"
    elif self.nilai >= 60:
        return "D"
    else:
        return "E"

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Nim: {self.nim}")
    print(f"Nilai: {self.nilai}")
    print(f"Nilai Huruf: {self.nilai_huruf()}")

mhs1 = Mahasiswa("Andi", "12345", 85)
mhs1.tampilkan_info()

mhs2 = Mahasiswa("Budi", "67890", 90)
mhs2.tampilkan_info()

# Tetap gunakan class Mahasiswa yang sudah kamu buat (dengan method tampilkan_info() dan nilai_huruf()).
# Buat list yang isinya beberapa object Mahasiswa.
# Gunakan perulangan for untuk menampilkan data semua mahasiswa.

class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self.nim = nim
    self.nilai = nilai
  
  def nilai_huruf(self):
    if self.nilai >= 90:
        return "A"
    elif self.nilai >= 80:
        return "B"
    elif self.nilai >= 70:
        return "C"
    elif self.nilai >= 60:
        return "D"
    else:
        return "E"

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Nim: {self.nim}")
    print(f"Nilai: {self.nilai}")
    print(f"Nilai Huruf: {self.nilai_huruf()}")

daftar_mahasiswa = [
    Mahasiswa("Andi", "12345", 85),
    Mahasiswa("Budi", "67890", 90),
    Mahasiswa("Cici", "11223", 72)
]

for mhs in daftar_mahasiswa:
    mhs.tampilkan_info()
    print("-" * 30) 

# Minta user input nama, NIM, dan nilai lewat keyboard.
# Simpan data mahasiswa ke dalam list.
# Tampilkan semua data yang telah diinput.

class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self.nim = nim
    self.nilai = nilai
  
  def nilai_huruf(self):
    if self.nilai >= 90:
        return "A"
    elif self.nilai >= 80:
        return "B"
    elif self.nilai >= 70:
        return "C"
    elif self.nilai >= 60:
        return "D"
    else:
        return "E"

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Nim: {self.nim}")
    print(f"Nilai: {self.nilai}")
    print(f"Nilai Huruf: {self.nilai_huruf()}")

# =========== input data dari mahasiswa =========== 
daftar_mahasiswa = []

jumlah = int(input("masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = int(input("Nilai: "))

    mhs = Mahasiswa(nama, nim, nilai)
    daftar_mahasiswa.append(mhs)

# ==== Tampilkan data mahasiswa ====
print("\n=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    mhs.tampilkan_info()
    print("-" * 30)

# Tambah Mahasiswa
# Tampilkan Semua Mahasiswa
# Keluar

class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def nilai_huruf(self):
        if self.nilai >= 90:
            return "A"
        elif self.nilai >= 80:
            return "B"
        elif self.nilai >= 70:
            return "C"
        elif self.nilai >= 60:
            return "D"
        else:
            return "E"

    def tampilkan_info(self):
        print(f"Nama        : {self.nama}")
        print(f"NIM         : {self.nim}")
        print(f"Nilai       : {self.nilai}")
        print(f"Nilai Huruf : {self.nilai_huruf()}")


# List untuk menyimpan data mahasiswa
daftar_mahasiswa = []

# Menu interaktif
while True:
    print("\n=== MENU ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Daftar Mahasiswa")
    print("3. Cari Mahasiswa berdasarkan NIM")
    print("4. Cari Mahasiswa berdasarkan Nama")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        print("\n== Tambah Mahasiswa ==")
        nama = input("Nama  : ")
        nim = input("NIM   : ")
        nilai = int(input("Nilai : "))
        
        mhs = Mahasiswa(nama, nim, nilai)
        daftar_mahasiswa.append(mhs)
        print("✅ Mahasiswa berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n== Daftar Mahasiswa ==")
        if len(daftar_mahasiswa) == 0:
            print("❗ Belum ada data mahasiswa.")
        else:
            for mhs in daftar_mahasiswa:
                mhs.tampilkan_info()
                print("-" * 30)

    elif pilihan == "3":
        print("\n== Cari Mahasiswa Berdasarkan NIM ==")
        cari_nim = input("Masukkan NIM: ")
        ditemukan = False

        for mhs in daftar_mahasiswa:
            if mhs.nim == cari_nim:
                print("\n✅ Data Mahasiswa Ditemukan:")
                mhs.tampilkan_info()
                print("-" * 30)
                ditemukan = True
                break

        if not ditemukan:
            print("❗ Mahasiswa dengan NIM tersebut tidak ditemukan.")

    elif pilihan == "4":
        print("\n== Cari Mahasiswa Berdasarkan Nama ==")
        cari_nama = input("Masukkan Nama: ")
        ditemukan = False

        for mhs in daftar_mahasiswa:
            if mhs.nama.lower() == cari_nama.lower():
                print("\n✅ Data Mahasiswa Ditemukan:")
                mhs.tampilkan_info()
                print("-" * 30)
                ditemukan = True
                break

        if not ditemukan:
            print("❗ Mahasiswa dengan nama tersebut tidak ditemukan.")

    elif pilihan == "5":
        print("\nTerima kasih ya sayang udah pake program ini 😘💖")
        break

    else:
        print("⚠️ Pilihan tidak valid! Coba lagi.")
