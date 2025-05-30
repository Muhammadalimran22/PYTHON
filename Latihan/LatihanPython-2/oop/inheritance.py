class AkunBank:
  def __init__(self, saldo):
    self.__saldo = saldo

  def lihat_saldo(self):
    print(f"saldo saat ini: {self.__saldo}")
  
  def tarik(self, jumlah):
    if jumlah <= self.__saldo:
      self.__saldo -= jumlah
    else:
      print("saldo tidak cukup")

akun = AkunBank(10000)
akun.lihat_saldo()
akun.tarik(5000)
akun.lihat_saldo()