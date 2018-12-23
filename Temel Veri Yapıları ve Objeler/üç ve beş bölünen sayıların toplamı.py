toplam = 0

# liste = [x for x in range(1,1001) if x % 3 == 0 if y % 5 == 0]
# liste = [y for y in [x for x in range(1,1001) if x % 3 == 0] if y % 5 == 0]

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        toplam += i

print("Toplam:",toplam)