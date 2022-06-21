def mukemmelsayi(x):
    toplam = 0
    for i in range(1, x):
        if (x % i == 0):
            toplam += i
    if (x == toplam):
        return True
    else:
        return False

(z,j) = input("Arama yapacağınız aralığı girin [x,y]: ").split(",")

for x in range(int(z), int(j)):
    if mukemmelsayi(x) == True:
        print (f"{x} bir mükemmel sayıdır.")