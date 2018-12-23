class Basketci():
    def __init__(self,ad,soyad,boy,basket_ortalamasi,maas):
        self.ad = ad
        self.soyad = soyad
        self.boy = boy
        self.basket_ortalamasi = basket_ortalamasi
        self.maas = maas
    def bilgileri_goster(self):
        print("""
        Basketçi Özellikleri
        Ad \t\t\t\t\t: {}
        Soyad \t\t\t\t: {}
        Boy (cm)\t\t\t: {}
        Basket Ort.[SA,2,3]\t: {}
        Maaş \t\t\t\t: {}
        """.format(self.ad,self.soyad,self.boy,self.basket_ortalamasi,self.maas))
    def zam_yap(self,zam_miktari):
        print("Zam yapılıyor...")
        self.maas += zam_miktari
    def basket_ort_degistir(self,sa,ia,ua):
        print("Ortalamalar güncelleniyor...")
        if self.basket_ortalamasi[0] != sa:
            self.basket_ortalamasi[0] = sa
        if self.basket_ortalamasi[1] != ia:
            self.basket_ortalamasi[1] = ia
        if self.basket_ortalamasi[2] != ua:
            self.basket_ortalamasi[2] = ua

basketci1 = Basketci("Erol","Kahraman",170,[20,21,25],3000)

basketci1.zam_yap(2000)

basketci1.basket_ort_degistir(20,22,30)

print(basketci1.bilgileri_goster())


