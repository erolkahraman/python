"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
toplam = 0

sayi = input("Bir sayı giriniz: ")
basamak_sayisi = len(sayi)
print(basamak_sayisi)

sayi_dizisi = list(sayi)
print(sayi_dizisi)

for i in sayi_dizisi:
    toplam += int(i) ** basamak_sayisi

if (int(sayi) == toplam):
    print("Bu bir Armstrong sayısıdır...")

print("Toplam=",toplam)
