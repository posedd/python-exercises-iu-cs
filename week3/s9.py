# Belirli bir aralıktaki sayıları içeren bir liste oluşturan bir fonksiyon yazınız.
# Klavyeden girilen matris tipine göre elemanları 0-9 arasında rastgele tam sayılardan
# oluşan ve sütun elemanları toplamı eşit olan programı yazınız.

def aralikli_liste(bas, son):
    liste = []
    for i in range(bas,son):
         liste.append(i)
    return liste
print(aralikli_liste(1,9))
