dizi = list()
sayi = int(input("bir sayı girin:"))

for i in range(1,sayi // 2):
    if (sayi % i == 0):
        dizi.append(i)

print(dizi)