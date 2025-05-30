class Hewan:
    def suara(self):
        print("Hewan bersuara...")

class Kucing(Hewan):
    def suara(self):
        print("Meong~")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk~")

# Fungsi polymorphism
def buat_suara(hewan):
    hewan.suara()

buat_suara(Kucing())
buat_suara(Anjing())
