for i in range(1,51):
    for j in range(2,i):
        if (j <= i //2 and i % j == 0):
            break
        else:
            if (j == i//2 + 1):
                print(i)

