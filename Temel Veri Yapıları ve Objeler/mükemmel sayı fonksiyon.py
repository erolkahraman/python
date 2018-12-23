def mukemmel_sayi_bulma():
    mukemmel_sayilar = list()
    for sayi in range(1,1001):
        bolenler = list()
        toplam = 0
        for bolen in range(1,sayi):
            if sayi % bolen == 0:
                bolenler.append(bolen)
        for i in bolenler:
            toplam += i
        if sayi == toplam:
            mukemmel_sayilar.append(sayi)
    return mukemmel_sayilar
print(mukemmel_sayi_bulma())
