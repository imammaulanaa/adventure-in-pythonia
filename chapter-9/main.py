from adventure_manager import AdventureManager

def main():
    manager = AdventureManager()
    data = manager.load_data()

    print("=== Daftar Petualang ===")
    for petualang in data:
        print(f"- {petualang['nama']} (Level: {petualang['level']}, Kekuatan: {petualang['kekuatan']})")

if __name__ == "__main__":
    main()
