import json
from file_manager import baca_json, tulis_json, tulis_log

class AdventureManager:
    def __init__(self, data_file="data/petualang_data.json", log_file="data/petualang_log.txt"):
        self.data_file = data_file
        self.log_file = log_file

    def load_data(self):
        return baca_json(self.data_file)

    def add_petualang(self, petualang):
        data = self.load_data()
        data.append(petualang)
        tulis_json(self.data_file, data)
        tulis_log(self.log_file, f"Petualang baru ditambahkan: {petualang['nama']}")
