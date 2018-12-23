"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
print("""
#################################
#
#   Mükemmel Sayı Hesaplama
#
#################################
""")
bolen = 1
toplam = 0
carpanlar = list()

sayi = int(input("Bir sayı giriniz: "))
while (bolen <= (sayi // 2)):
    if (not (sayi % bolen)):
        carpanlar.append(bolen)
        bolen += 1
    else:
        bolen += 1
for i in carpanlar:
    toplam += i
if (toplam == sayi):
    print (sayi, "Mükemmel bir sayı buldunuz...")
print(carpanlar)

