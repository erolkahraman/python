class Araba():
    def __init__(self,model = "Bilgi yok1",tescil_tarihi = "Bilgi yok2",beygir_gucu = "Bilgi yok3"):
        self.model = model
        self.tescil_tarihi = tescil_tarihi
        self.beygir_gucu = beygir_gucu
        print("init fonksiyonu çağırıldı.")

araba1 = Araba(2006,1020,"deneme1")
araba2 = Araba(2008,2000,"deneme2")
araba3 = Araba(model = 2001)

print(araba1.model)
print(araba2.model)
print(araba3.beygir_gucu)