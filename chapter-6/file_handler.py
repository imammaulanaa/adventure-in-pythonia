def baca_mantra():
    try:
        with open("data/mantra.txt", "r") as file:
            return [baris.strip() for baris in file.readlines()]
    except FileNotFoundError:
        return []

def simpan_mantra(mantra):
    with open("data/mantra.txt", "a") as file:
        file.write(mantra + "\n")
