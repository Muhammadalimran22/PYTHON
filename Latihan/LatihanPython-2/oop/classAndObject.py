class Mobil:
  def __init__(self, merk, warna):
    self.merk = merk
    self.warna= warna

  def info(self):
    print(f"mobil {self.merk} berwarna {self.warna}")
  

mobil_saya = Mobil("toyota", "merah")
mobil_saya.info()