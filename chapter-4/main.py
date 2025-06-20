class Petualangan:
    def __init__(self, nama, tingkat_kesulitan):
        self.nama = nama
        self.tingkat_kesulitan = tingkat_kesulitan

    def info(self):
        return f"Petualangan: {self.nama}, Tingkat Kesulitan: {self.tingkat_kesulitan}"

def tampilkan_menu():
    print("=== Sistem Pencatat Petualangan Pythorius ===")
    print("1. Tambah Petualangan")
    print("2. Lihat Semua Petualangan")
    print("3. Keluar")

def main():
    daftar_petualangan = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            nama = input("Nama petualangan: ")
            tingkat = input("Tingkat kesulitan (mudah/sedang/sulit): ")
            petualangan_baru = Petualangan(nama, tingkat)
            daftar_petualangan.append(petualangan_baru)
            print("Petualangan berhasil ditambahkan!\n")
        elif pilihan == '2':
            if daftar_petualangan:
                print("\nDaftar Petualangan:")
                for i, petualangan in enumerate(daftar_petualangan, 1):
                    print(f"{i}. {petualangan.info()}")
                print("")
            else:
                print("Belum ada petualangan yang tercatat.\n")
        elif pilihan == '3':
            print("Sampai jumpa, penjelajah Pythorius!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main()
