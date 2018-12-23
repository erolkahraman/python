"""
Kullanıcı üç sayı girişi yapıyor.
Program en büyükten en küçüğe doğru sıralıyor.
"""

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
c = int(input("Üçüncü sayı: "))

if a > b and a > c:
    if b > c:
        print ("{} > {} > {}".format(a, b, c))
    else:
        print("{} > {} > {}".format(a, c, b))
if b > a and b > c:
    if a > c:
        print ("{} > {} > {}".format(b, a, c))
    else:
        print("{} > {} > {}".format(b, c, a))
if c > a and c > b:
    if a > b:
        print ("{} > {} > {}".format(c, a, b))
    else:
        print("{} > {} > {}".format(c, b, a))