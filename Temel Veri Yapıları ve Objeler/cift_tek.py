def cift_mi(sayi):
    if sayi % 2 == 0:
        #print("%s çift sayıdır." % sayi)
        return sayi
    else:
        raise ValueError("Deneme hatası")


liste = [1,3,4,6,9,66,7,88,98,99]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass