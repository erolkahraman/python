for i in range(5000):
    toplam = 0
    basamak_sayisi = len(str(i))
#    sayi_dizisi = list(str(i))
    sayi_dizisi = [int(d) for d in str(i)]
    for rakam in sayi_dizisi:
        toplam += int(rakam) ** basamak_sayisi
    if (int(i) == toplam):
        print(i,"Bu bir Armstrong sayısıdır...")