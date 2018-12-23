def sayi_okuma(sayi):
    print(type(sayi))
    birler_basamagi = {1:"bir",
                     2:"iki",
                     3:"üç",
                     4:"dört",
                     5:"beş",
                     6:"altı",
                     7:"yedi",
                     8:"sekiz",
                     9:"dokuz",
                     0:"sıfır"}
    onlar_basamagi = {10:"on",
                      20:"yirmi",
                      30:"otuz",
                      40:"kırk",
                      50:"elli",
                      60:"altmış",
                      70:"yetmiş",
                      80:"seksen",
                      90:"doksan"}
    sayi = str(sayi)
    print(type(sayi))
    basamaklar = list(sayi)
    print(basamaklar)
    if birler_basamagi[int(basamaklar[1])] == "sıfır":
        print(onlar_basamagi[(int(basamaklar[0]) * 10)])
    else:
        print(onlar_basamagi[(int(basamaklar[0]) * 10)],birler_basamagi[int(basamaklar[1])])

sayi_okuma(15)
