# Bir listedeki tüm elemanların kareköklerinin ortalamasını hesaplayan bir
# fonksiyon yazın.
import math
liste = [1, 4, 9, 16, 25]

karekok_toplam=0
for sayi in liste:
    karekok_toplam += math.sqrt(sayi)
ortalama = karekok_toplam/len(liste)
print(ortalama)
