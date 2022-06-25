from datetime import date as d
date = d.today()

ad = str(input("Adınızı girin."))
soyad = str(input("Soyadınızı girin."))
gün = int(input("Doğum gününüzü girin."))
ay = int(input("Doğum ayınızı girin."))
yıl = int(input("Doğum yılınızı girin."))
tarih = [gün , ay , yıl]
yaş = ((date.year - yıl), (date.month - ay), (date.day - gün))
print(tarih)
print(yaş)
if date.year - yıl < 18 :
    print("Adınız:", ad)
    print("Soyadınız:", soyad)
    print("Doğum tarihiniz:", tarih)
    print("{} {} {} yaşında bir çocuksunuz.".format(ad,soyad,date.year - yıl))
elif 18 < date.year - yıl < 65 :
    print("Adınız:", ad)
    print("Soyadınız:", soyad)
    print("Doğum tarihiniz:", tarih)
    print("{} {} {} yaşında bir yetişkinsiniz.".format(ad, soyad, date.year - yıl))
elif 65 < date.year - yıl:
    print("Adınız:", ad)
    print("Soyadınız:", soyad)
    print("Doğum tarihiniz:", tarih)
    print("{} {} {} yaşında bir yaşlısınız.".format(ad, soyad, date.year - yıl))

kullanicibilgi = open(r"kullanıcı_bilgi.txt".encode("utf-8") ,"w")
kullanicibilgi.write("ad: {} soyad: {}  traih: {}".format(ad , soyad, tarih))
kullanicibilgi.close()