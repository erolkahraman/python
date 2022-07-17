import math
import random
from yukseklik import yukseklik as yk

puan = 0
atis_hakki = 3
print(type(atis_hakki))
a = random.randint(30, 170)
print(f"Hedefin merkez noktası: {a}")
print(f"Toplam atış hakkınız: {atis_hakki}")

while atis_hakki > 0:
    print("Kalan atış hakkınız:",atis_hakki)
    aci_degeri = int(input("Lütfen atış açısını giriniz: "))
    hiz_degeri = int(input("Lütfen çıkış hızını giriniz: "))
    mesafe_degeri = int(input("Lütfen hedefe olan uzaklığı giriniz(varsayılan 100 m): "))
    b = yk(aci_degeri,hiz_degeri,mesafe_degeri)
    if (0 <(abs(a-b))<= 10):
        puan += 20
        atis_hakki -= 1
        print("="*40)
        print(f"Hedefin merkezine olan uzaklığınız: {round(abs(a-b),1)}")
        print("Tebrikler! Puanınız: 20")
        print("="*40)
    elif (10 <(abs(a-b))<= 20):
        puan += 15
        atis_hakki -= 1
        print("="*40)
        print(f"Hedefin merkezine olan uzaklığınız: {round(abs(a-b),1)}")
        print("Tebrikler! Puanınız: 15")
        print("="*40)
    elif (20 <(abs(a-b))<= 30):
        puan += 10
        atis_hakki -= 1
        print("="*40)
        print(f"Hedefin merkezine olan uzaklığınız: {round(abs(a-b),1)}")
        print("Tebrikler! Puanınız: 10")
        print("="*40)
    else:
        puan += 0
        atis_hakki -= 1
        print("="*40)
        print(f"Hedefin merkezine olan uzaklığınız: {round(abs(a-b),1)}")
        print("Hedefi vuramadınız! Puanınız: 0")
        print("="*40)

print(f"Tebrik ederiz. Toplam puanınız: {puan}")