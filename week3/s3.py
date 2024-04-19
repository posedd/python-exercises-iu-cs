# Verilen bir sayının çarpanlarını liste olarak veren fonksiyon yazınız.

def carpanbul(sayi):
    carpanlar = []
    for i in range(1,sayi+1):
        if sayi%i == 0:
            carpanlar.append(i)
    return carpanlar
#print(carpanbul(36))