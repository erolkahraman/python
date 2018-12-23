"""
Beden kitle indeksi = kilo / boy ** 2

bki < 18.5 --> zayıf
18.5 < bki < 25 --> normal
25 < bki < 30 --> fazla kilolu
30 < bki --> obez
"""

print("Beden Kitle Endeksi Hesaplama")
boy = int(input("Lütfen boyunuzu giriniz (cm): "))
kilo = int(input("Lütfen kilonuzu giriniz (kg): "))
bki = kilo // ((boy/100) ** 2)

if (bki <= 18.5):
    print (bki, "Zayfsınız...")
elif (bki > 18.5 and bki < 25):
    print (bki, "Normal kilodasınız...")
elif (bki >= 25 and bki < 30 ):
    print (bki, "Fazla kilonuz var...")
else:
    print (bki, "Az ye dana...")