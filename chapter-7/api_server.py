from flask import Flask, jsonify, request

app = Flask(__name__)

# Data petualang (dummy)
petualang = [
    {"id": 1, "nama": "Pythorius", "level": 5},
    {"id": 2, "nama": "Lyra", "level": 3}
]

@app.route('/petualang', methods=['GET'])
def get_petualang():
    return jsonify(petualang)

@app.route('/petualang', methods=['POST'])
def tambah_petualang():
    data = request.get_json()
    petualang.append(data)
    return jsonify({"pesan": "Petualang berhasil ditambahkan!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
