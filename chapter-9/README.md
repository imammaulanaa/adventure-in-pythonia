# Chapter 9 – Puncak Petualangan dan Sistem Manajemen Petualang
Pythorius akhirnya tiba di Puncak Pythonia, tempat tertinggi yang hanya bisa dicapai oleh penjelajah sejati. Di sini, ia dihadapkan pada misi besar: membangun Sistem Manajemen Petualang untuk mendata semua penyihir dan petualang yang pernah menapaki jejak petualangan di dunia ini.
Pythorius harus menggunakan semua ilmu yang telah ia pelajari: struktur data, fungsi, OOP, validasi, file handling, dan lainnya. Semua petualang akan disimpan dalam file JSON, dan sistem ini akan menjadi warisan abadi bagi generasi penjelajah berikutnya.
---
## 1. Struktur Data Petualang
Setiap petualang memiliki nama, level, dan daftar mantra.
## 2. Menyimpan dan Membaca dari File JSON
Pythorius menggunakan JSON untuk menyimpan data petualang agar dapat dibaca kembali kapan saja.
## 3. Main Program: Tambah & Tampilkan Petualang
**Struktur Folder**

```bash
chapter-9/
├── api_server.py
├── adventure_manager.py
├── character.py
├── file_manager.py
├── utils.py
├── main.py
└── data/
    ├── petualang_data.json
    └── petualang_log.txt
```
**Cara Menjalankan**
-  Menjalankan Program Utama (CLI)
Untuk melihat daftar petualang melalui terminal, jalankan perintah:
```bash
python main.py
```
Output:
```php
=== Daftar Petualang ===
- Pythorius (Level: 5, Kekuatan: 150)
- Zephyra (Level: 3, Kekuatan: 120)
```

-  Menjalankan API Server (Flask)
Untuk mengaktifkan server API:
```bash
python api_server.py
```
Server akan berjalan di:
```cpp
http://localhost:5000/
```
API Endpoint
- GET /petualang → Mendapatkan daftar petualang.

- POST /petualang → Menambahkan petualang baru.

Contoh POST dengan JSON:
```json
{
    "nama": "Lyra",
    "level": 4,
    "kekuatan": 130
}
```
---

Pythorius kini menjadi penjaga Puncak Pythonia dan pencatat resmi semua petualangan.
Dengan sistem manajemen ini, kisah para petualang akan hidup selamanya dalam lembaran digital yang tertata rapi.

Petualangan selesai, tapi perjalanan belajar masih terus berlanjut...