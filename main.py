import random

uzunluk = int(input("uzunluk ne kadar olsun? "))

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
shuffled_chars = karakterler.join("")
random.shuffle(shuffled_chars)

sifre = ""

for i in range(uzunluk):
    karakter = random.choice(karakterler)
    sifre = sifre + karakter

print(f"{uzunluk} karakter uzunluğunda bir şifre oluşturuldu.")
print(sifre)
