# Random kütüphanesi kullanarak bir zar oyunu simüle edin. 2 zar atılsın.
# Yazılan fonksiyon atılan zarlarda denk gelen sayıların toplamını versin.

import random
def zar_at():
    zar1 = random.randint(1,6)
    zar2 = random.randint(1, 6)
    toplam = zar1 + zar2
    return toplam
print(zar_at())