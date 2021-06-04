def asal_mi(sayi):
    sayac = 0
    for i in range(2,(sayi + 1)):
        if not sayi % i:
            sayac += 1
        else:
            continue
    if sayac == 1:
        return True
    else:
        return False

def dongusel_asal(sayi):
    ters_sayi = ""
    if sayi < 10:
        print("{} Dongüsel asal...".format(sayi))
    else:
        rakamlar = list(str(sayi))
        for  i in rakamlar[::-1]:
            ters_sayi += i
        if asal_mi(int(ters_sayi)):
            print("{} Dongüsel asal...".format(sayi))
            

for i in range(100):
    if asal_mi(i) and dongusel_asal(i):
        continue





