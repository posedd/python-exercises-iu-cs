# Bir listedeki tüm elemanların mutlak değerlerinin çarpımını hesaplayan bir
# fonksiyon yazın.

from math import fabs
def mutlak_carpim(liste):
    carpim=1
    for sayi in liste:
        carpim *= fabs(sayi)
    return carpim

liste = [2,-8,8]
print(mutlak_carpim(liste))