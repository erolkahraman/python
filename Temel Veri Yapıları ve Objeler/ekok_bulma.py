def ekok_bulma(a,b):
    a_kat = []
    b_kat = []
    print("1-",a,b,a * b)
    for i in range(1,(a * b + 1)):
        a_kat.append(i * a)
        print("2-",a_kat)
        if i * a == a * b:
            break 
    for j in range(1,(a * b + 1)):
        b_kat.append(j * b)
        print("3-",b_kat)
        if j * b == a * b:
            break
    for x in a_kat:
        for y in b_kat:
            if x == y:
                ekok = x
                print("6-",ekok)
                break
        if x == y:
            break

    print ("5-",x)
    #print(a_kat,b_kat)
ekok_bulma(21,49)

