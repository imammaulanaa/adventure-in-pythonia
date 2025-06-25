class Character:
    def __init__(self, nama, level, kekuatan):
        self.nama = nama
        self.level = level
        self.kekuatan = kekuatan

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Level: {self.level}, Kekuatan: {self.kekuatan}"
