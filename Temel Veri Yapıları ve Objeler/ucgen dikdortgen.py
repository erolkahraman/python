print ("1. Üçgen\n2. Dikdörtgen")
secim = int(input("Seçiminiz: "))

if (secim == 1):
    a = int(input("1.kenar uzunluğu: "))
    b = int(input("2.Kenar uzunluğu: "))
    c = int(input("3.Kenar uzunluğu: "))
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if (a == b) and (b == c):
            print ("Bu bir eşkenar üçgendir.")
        elif (a == b) or (b == c) or (c == b):
            print("Bu bir ikizkenar üçgendir")
        else:
            print("Bu bir çeşitkenar üçgendir.")
    else:
        print("Bu ölçülerde bir üçgen olamaz.")
else:
    a = int(input("1.kenar uzunluğu: "))
    b = int(input("2.Kenar uzunluğu: "))
    c = int(input("3.Kenar uzunluğu: "))
    d = int(input("d.Kenar uzunluğu: "))
    if (a == b == c == d):
        print("Bu bir karedir.")
    elif (a == c) and (b ==d):
        print("Bu bir dikdörtgendir.")
    else:
        print("Bu bir dörtgendir.")