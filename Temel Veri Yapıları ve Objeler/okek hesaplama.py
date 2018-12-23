def okek_hesaplama(sayi1,sayi2):
    sayi1_bolenler = list()
    sayi2_bolenler = list()

    while True:
        for i in range(2,(sayi1 // 2) + 1):
            if sayi1 / i == int(sayi1 / i):
                sayi1_bolenler.append(i)
                sayi1 /= i
                break
    print (sayi1_bolenler)

okek_hesaplama(12,5)