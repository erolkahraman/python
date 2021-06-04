while True:

    print("""
    
    ======== MENU ========

    1. Kayıt
    2. Sorgulama
    3. Şifreli Giriş

    q. Çıkış
    
    """)    
    cevap = input("İşlem Seçiniz: ")
    if cevap == "q":
        break

def kayit():
    user_name = input("Kullanıcı Adı: ")
    user_surname = input("Kullanıcı Soyadı:")
    nickname = input("Rumuz: ")
    password = input("Şifre: ")
    re_password = input("Şifre tekrar: ")

user1 = {}

user1 ["user_name"] = "erol"

print(user1["user_name"])

