import json
from datetime import datetime

def baca_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def tulis_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def tulis_log(log_file, pesan):
    with open(log_file, "a") as file:
        file.write(f"[{datetime.now()}] {pesan}\n")
