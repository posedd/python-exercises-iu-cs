# Fibonacci serisini rekürsif olmayan bir yöntem kullanarak hesaplayın. Liste yapıları ve fonksiyon tanımı bulunmayan bir program yazınız.
# Fibonacci serisi, önceki iki terimin toplamıyla oluşturulan bir seridir: 0, 1, 1, 2, 3, 5, 8, 13, …

a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a+b