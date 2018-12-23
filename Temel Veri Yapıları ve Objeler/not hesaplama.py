"""
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""

vize1 = int(input("1. Vize notu: "))
vize2 = int(input("2. Vize notu: "))
final = int(input("Final notu: "))

gecme_notu = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if gecme_notu >= 90:
    print("Notunuz {} = AA".format(gecme_notu))
elif gecme_notu >= 85 and gecme_notu < 90:
    print ("Notunuz {} = BA".format(gecme_notu))
elif gecme_notu >=80 and gecme_notu < 85:
    print ("Notunuz {} = BB".format(gecme_notu))
elif gecme_notu >=75 and gecme_notu < 80:
    print ("Notunuz {} = BC".format(gecme_notu))
elif gecme_notu >=70 and gecme_notu < 75:
    print ("Notunuz {} = CC".format(gecme_notu))
elif gecme_notu >=65 and gecme_notu < 70:
    print ("Notunuz {} = CD".format(gecme_notu))
elif gecme_notu >=60 and gecme_notu < 65:
    print ("Notunuz {} = DD".format(gecme_notu))
else:
    print ("Notunuz {} = FF".format(gecme_notu))