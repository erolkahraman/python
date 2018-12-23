print("HESAP MAKİNESİ")
print("1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme\n")
birinci_sayi = int(input("Birinci sayı: "))
ikinci_sayi = int(input("İkinci sayı: "))
islem = int(input("Yapmak istediğiniz işlem: "))

if (islem == 1):
    print ("{} ile {} toplamı = {}".format(birinci_sayi,ikinci_sayi,birinci_sayi+ikinci_sayi))
elif (islem == 2):
    print("{} ile {} farkı = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi - ikinci_sayi))
elif (islem == 3):
    print("{} ile {} çarpımı = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi * ikinci_sayi))
elif (islem == 4):
    print("{} ile {} bölümü = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi / ikinci_sayi))
else:
    print("Geçersiz bir seçim yaptınız...")