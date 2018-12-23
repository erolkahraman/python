def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob

print(ebob_bulma(24,48))