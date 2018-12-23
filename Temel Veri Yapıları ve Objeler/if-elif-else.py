sinav_notu = int(input("Sınav notunu giriniz: "))

if sinav_notu >= 90:
    print ("A aldınız")
elif sinav_notu >= 80 and sinav_notu <90:
    print ("B aldınız")
elif sinav_notu >= 70 and sinav_notu <80:
    print("C aldınız")
elif sinav_notu >=60 and sinav_notu <70:
    print("D aldınız")
else:
    print("Sınavdan kaldınız...")