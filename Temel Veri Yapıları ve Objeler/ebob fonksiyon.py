def ebob(a,b):
    ebob_listesi = list()
    if b > a:
        a,b = b,a
    k = a
    while k > 1:
        print("000")
        for i in range(2,int(a)+ 1):
            print("0.",i)
            if int(a) % i == 0 and int(b) % i == 0:
                print("1.",a,b)
                ebob_listesi.append(i)
                print(ebob_listesi)
                a /= i
                b /= i
                break
            else:
                print("2",k)
                k -= 1
    return ebob_listesi

print("11", ebob(11,12))