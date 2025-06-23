from datetime import datetime

def log_petualangan(kegiatan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/log_petualang.txt", "a") as file:
        file.write(f"[{waktu}] {kegiatan}\n")
