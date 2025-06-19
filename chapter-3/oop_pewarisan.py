class Penjelajah:
    def __init__(self, nama):
        self.nama = nama

    def aksi(self):
        print(f"{self.nama} menjelajah dunia Pythonia")

class Penyihir(Penjelajah):
    def sihir(self):
        print(f"{self.nama} mengeluarkan bola api!")

Pythorius = Penyihir("Pythorius")
Pythorius.aksi()
Pythorius.sihir()
