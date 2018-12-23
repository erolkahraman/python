"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""

liste = [x for x in range(100) if x % 3 == 0]
print(liste)