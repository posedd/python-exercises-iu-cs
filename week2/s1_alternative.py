# Armstrong sayıları, sayıların rakamlarının küplerinin toplamı, sayının kendisine eşit olduğunda oluşur.
# Örneğin, 153 = 1^3 + 5^3 + 3^3 olduğu için bir Armstrong sayısıdır.
# 1-1000 aralığındaki Armstrong sayılarını bulun.

for i in range(1,1000):
    sayi=i
    basamak_sayisi=len(str(sayi))
    #print(sayi, basamak_sayisi)

    if basamak_sayisi == 2:
        birler = sayi % 10
        onlar = int((sayi / 10) % 10)
        if sayi == birler ** 3 + onlar ** 3:
            print(sayi)
    elif basamak_sayisi == 3:
        birler = int(sayi%10)
        onlar = int((sayi/10)%10)
        yuzler = int((sayi/100)%10)
        if sayi == birler ** 3 + onlar ** 3 + yuzler ** 3:
            print(sayi)

