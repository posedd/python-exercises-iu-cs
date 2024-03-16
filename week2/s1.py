# Armstrong sayıları, sayıların rakamlarının küplerinin toplamı, sayının kendisine eşit olduğunda oluşur.
# Örneğin, 153 = 1^3 + 5^3 + 3^3 olduğu için bir Armstrong sayısıdır.
# 1-1000 aralığındaki Armstrong sayılarını bulun.

for i in range(1,1001):
    toplam=0
    temp=i
    while temp>0:
        digit=temp%10
        toplam+=digit**3
        temp//=10
        #print(i)
    if toplam==i:
        print(i)
