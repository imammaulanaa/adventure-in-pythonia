from file_handler import baca_mantra, simpan_mantra
from logger import log_petualangan
from utils import validasi_input

def main():
    print("Selamat datang di Kota Modular, Pythorius!")
    mantra_baru = input("Masukkan mantra baru yang ingin disimpan: ")

    if validasi_input(mantra_baru):
        simpan_mantra(mantra_baru)
        log_petualangan(f"Mantra '{mantra_baru}' telah disimpan.")
        print("Mantra berhasil disimpan!")
    else:
        print("Mantra tidak valid, coba lagi.")

    print("\nMantra yang tersimpan:")
    daftar_mantra = baca_mantra()
    for mantra in daftar_mantra:
        print("-", mantra)

if __name__ == "__main__":
    main()
