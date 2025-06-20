import json
import os

DATA_DIR = "data"
FILE_JSON = os.path.join(DATA_DIR, "petualangan.json")
FILE_LOG = os.path.join(DATA_DIR, "log_petualangan.txt")

def buat_folder_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def simpan_petualangan_json(petualangan_list):
    with open(FILE_JSON, "w") as f:
        json.dump(petualangan_list, f, indent=4)
    print("Data petualangan berhasil disimpan dalam JSON.")

def baca_petualangan_json():
    if not os.path.exists(FILE_JSON):
        return []
    with open(FILE_JSON, "r") as f:
        return json.load(f)

def tambah_log(pesan):
    with open(FILE_LOG, "a") as f:
        f.write(pesan + "\n")
    print("Log petualangan ditambahkan.")

def main():
    buat_folder_data()
    petualangan_list = baca_petualangan_json()

    while True:
        print("=== Perpustakaan Data Pythonia ===")
        print("1. Tambah petualangan")
        print("2. Lihat petualangan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            nama = input("Nama petualangan: ")
            tingkat = input("Tingkat kesulitan: ")
            petualangan_list.append({"nama": nama, "tingkat_kesulitan": tingkat})
            simpan_petualangan_json(petualangan_list)
            tambah_log(f"Petualangan '{nama}' dengan tingkat '{tingkat}' ditambahkan.")
            print("Petualangan baru berhasil dicatat!\n")
        elif pilihan == '2':
            if petualangan_list:
                print("\nDaftar Petualangan:")
                for idx, p in enumerate(petualangan_list, 1):
                    print(f"{idx}. {p['nama']} - Tingkat: {p['tingkat_kesulitan']}")
                print("")
            else:
                print("Belum ada petualangan yang tercatat.\n")
        elif pilihan == '3':
            print("Sampai jumpa, Pythorius!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main()
