def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Kullanıcıdan bir sayı alalım
sayi = int(input("Bir sayı girin: "))

# Asal sayı kontrolü yapalım
if asal_mi(sayi):
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")
