# Verilen bir değere kadar olan tüm tek sayıları bir dizi şeklinde döndüren
# fonksiyon yazınız.

def tek_sayi(n):
    tek_sayilar = []
    for i in range(1, n+1):
        if i%2 == 1:
            tek_sayilar.append(i)
    return tek_sayilar
#print(tek_sayi(10))
