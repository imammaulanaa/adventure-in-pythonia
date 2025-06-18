def hitung_kekuatan(n):
    if n == 1:
        return 1
    else:
        return n * hitung_kekuatan(n-1)

print("Hasil kekuatan:", hitung_kekuatan(5))
