def validasi_mantra(mantra):
    if len(mantra) < 3:
        return False
    if not mantra.replace(" ", "").isalpha():
        return False
    return True

inventori_mantra = []

def tambah_mantra(mantra):
    if validasi_mantra(mantra):
        inventori_mantra.append(mantra)
        print(f" Mantra '{mantra}' berhasil ditambahkan!")
    else:
        print(f" Mantra '{mantra}' tidak valid!")

def hapus_mantra(mantra):
    if mantra in inventori_mantra:
        inventori_mantra.remove(mantra)
        print(f" Mantra '{mantra}' telah dihapus.")
    else:
        print(f" Mantra '{mantra}' tidak ditemukan dalam inventori.")
