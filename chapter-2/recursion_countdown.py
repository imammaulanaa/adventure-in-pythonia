def mundur(n):
    if n <= 0:
        print("Sihir waktu selesai!")
    else:
        print(f"Mantra mundur: {n}")
        mundur(n-1)

mundur(5)
