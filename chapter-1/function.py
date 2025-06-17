# Fungsi tanpa parameter
def salam():
    print("Halo, penjelajah Pythonia!")

salam()

# Fungsi dengan parameter
def sapa(nama):
    print(f"Halo, {nama}! Selamat datang!")

sapa("Pythorius")

# Fungsi dengan return
def jumlahkan(a, b):
    return a + b

hasil = jumlahkan(3, 4)
print("Hasil jumlah:", hasil)
