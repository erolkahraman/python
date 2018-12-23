class Hayvanlar():
    def __init__(self,adi,yirtici_mi,otobur_mu,omurgali_mi,omur,tukenen_soy):
        self.adi = adi
        self.yirtici_mi = yirtici_mi
        self.otobur_mu = otobur_mu
        self.omurgali_mi = omurgali_mi
        self.omur = omur
        self.tukenen_soy = tukenen_soy
    def bilgileri_goster(self):
        print("""
        Hayvan Bilgileri
        Adı\t\t\t\t: {}
        Yırtıcı\t\t\t: {}
        Otobur\t\t\t: {}
        Omurgalı\t\t: {}
        Ömrü\t\t\t: {}
        Soyu Tükeniyor\t: {}
        """.format(self.adi,self.yirtici_mi,self.otobur_mu,self.omurgali_mi,self.omur,self.tukenen_soy))
class Kopekler(Hayvanlar):
    def __init__(self,adi="bilgi yok",yirtici_mi="bilgi yok",otobur_mu="bilgi yok",omurgali_mi="bilgi yok",omur="bilgi yok",tukenen_soy="bilgi yok",cins="bilgi yok"):
        super().__init__(adi,yirtici_mi,otobur_mu,omurgali_mi,omur,tukenen_soy)
        self.cins = cins
    def bilgileri_goster1(self):
        print("""
        Hayvan Bilgileri
        Adı\t\t\t\t: {}
        Yırtıcı\t\t\t: {}
        Otobur\t\t\t: {}
        Omurgalı\t\t: {}
        Ömrü\t\t\t: {}
        Soyu Tükeniyor\t: {}
        Köpek Cinsi \t: {}
        """.format(self.adi,self.yirtici_mi,self.otobur_mu,self.omurgali_mi,self.omur,self.tukenen_soy,self.cins))

hayvan1 = Hayvanlar("ASLAN","YIRTICI","OTOBUR DEĞIL","OMURGALI","20","SOYU TEHLIKEDE")

kopek1 = Kopekler("ASLAN","YIRTICI","OTOBUR DEĞIL","OMURGALI","20","SOYU TEHLIKEDE","Doberman")



print(hayvan1.bilgileri_goster())
print(kopek1.bilgileri_goster1())