from flask import Flask, jsonify, request
from adventure_manager import AdventureManager

app = Flask(__name__)
manager = AdventureManager()

@app.route("/")
def home():
    return jsonify({"message": "Selamat datang di API Petualangan Pythorius!"})

@app.route("/petualang", methods=["GET"])
def get_petualang():
    data = manager.load_data()
    return jsonify(data)

@app.route("/petualang", methods=["POST"])
def add_petualang():
    new_data = request.json
    manager.add_petualang(new_data)
    return jsonify({"message": "Petualang baru berhasil ditambahkan!"})

if __name__ == "__main__":
    app.run(debug=True)
