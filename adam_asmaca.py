import random
adamlar = ["""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |""" ,"""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
       |
       |
       |
=========""","""
   +---+
   |   |
       |
       |
       |
       |
========="""]

kelimeler = ["elma","armut","balık"]
kelime = random.choice(kelimeler)
kelime1 =list(kelime)
hak = 6
tahmini = len(kelime1) * "_"
l_tahmini = list(tahmini)
print(l_tahmini)

while True:
    harf = str(input("Harf giriniz: "))
    if (harf in kelime):
        print("Doğru buldun")
        yer = kelime1.index(harf)
        l_tahmini[yer] = harf
        print(*l_tahmini)
        if l_tahmini == kelime1:
            print("Bütün harfleri buldun.")
            break
    if (harf not in kelime):
        print(adamlar[hak] , "{} kadar hakkınız kaldı".format(hak))
        hak = hak -1
        if hak < 0 :
            print("Kaybettiniz.")
            break