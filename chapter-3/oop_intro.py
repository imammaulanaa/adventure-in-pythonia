class Penjelajah:
    def __init__(self, nama, level):
        self.nama = nama
        self.level = level

    def kenalkan(self):
        print(f"Aku {self.nama}, penjelajah level {self.level}")

Pythorius = Penjelajah("Pythorius", 3)
Pythorius.kenalkan()
