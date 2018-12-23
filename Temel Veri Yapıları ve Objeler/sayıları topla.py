toplam = 0

while True:
    sayi = input("Bir sayı giriniz (Çıkmak için \"q \"): ")
    if sayi == "q":
        break
    else:
        toplam += int(sayi)
print ("Toplam =",toplam)