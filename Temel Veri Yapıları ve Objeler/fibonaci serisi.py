a = 1
b = 1
i = 4000000
toplam = 0

while (i > 0):
    if b % 2 != 0:
        toplam += b
        print(b)
    (a,b) = (b,a+b)
    i -= 1
print(toplam)