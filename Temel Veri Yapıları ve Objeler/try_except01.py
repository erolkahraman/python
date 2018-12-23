liste = ["345","sadas","324a","14","kemal"]

for kelime in liste:
    try:
        if int(kelime):
            print(kelime)
    except:
        #print("%s : Değer hatası var" % (kelime))
        pass