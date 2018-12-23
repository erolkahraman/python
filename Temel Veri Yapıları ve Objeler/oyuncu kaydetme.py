print ("#"*40)
print ("##")
print ("##\t\tOYUNCU KAYIT PROGRAMI")
print ("##")
print ("#"*40)
ad = input("Oyuncu İsmi\t\t: ")
soyad = input("Oyunccu Soyismi\t: ")
takim = input ("Takım\t\t\t: ")

bilgiler = [ad,soyad,takim]
print("Bilgiler kaydediliyor...")

# print("Oyuncu Adı\t\t:{}\nOyuncu Soyadı\t:{}\nOyuncu Takımı\t:{}".format(ad,soyad,takim))
print("Oyuncu Adı\t\t:{}\nOyuncu Soyadı\t:{}\nOyuncu Takımı\t:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))