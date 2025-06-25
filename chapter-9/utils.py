def validasi_nama(nama):
    return isinstance(nama, str) and len(nama) > 0

def validasi_level(level):
    return isinstance(level, int) and level > 0

def validasi_kekuatan(kekuatan):
    return isinstance(kekuatan, int) and kekuatan > 0
