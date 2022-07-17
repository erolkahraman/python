import math

def yukseklik(aci: int, hiz: int, mesafe=100) -> int:
    """
    Fonksiyon belirlenen mesafedeki hedefe, belli bir açı ve hız ile 
    atıldığında ne kadar yaklaştığını hesaplamaktadır.
    aci: İlk çıkış noktasındaki hız bileşeninin yatay ile yaptığı açı.
    hiz: İlk çıkış noktasındaki hız bileşeni.
    mesafe: İlk çıkış noktası ile hedef arasındaki mesafedir.
    """
    g = 10
    ucus_suresi = round((mesafe /  (math.cos(math.radians(aci)) * hiz)),1)
    yatay_hiz = round(math.cos(math.radians(aci)) * hiz,1)
    dikey_hiz = round(math.sin(math.radians(aci)) * hiz,1)
    
    # print(f"""
    # Uçuş süresi\t\t: {ucus_suresi} sn
    # Uçuş mesafesi\t: {mesafe} m
    # Yatay Hız\t\t: {yatay_hiz} m/s
    # Dikey Hız\t\t: {dikey_hiz} m/s
    # """)

    y = round((math.sin(math.radians(aci)) * hiz * ucus_suresi) - (0.5 * g * pow(ucus_suresi,2)),1)
    return y

# print (f"Yerden yükseklik: {yukseklik(37,32.455,100)} m")