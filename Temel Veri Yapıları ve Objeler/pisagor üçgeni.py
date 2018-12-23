for a in range(1,101):
    for b in range(1,101):
        c = ((a ** 2 + b ** 2) ** 0.5)
        if int(c) == c:
            print("a:{},b:{},c:{:.2f}".format(a,b,c))
            print("bu bir pisagor üçgenidir")
            print("#"*15)
