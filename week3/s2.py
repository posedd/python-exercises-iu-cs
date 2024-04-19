# Verilen bir sayının basamaklarının sayı değerlerinin toplamının çift mi tek mi
# olduğunu bulan fonksiyon yazınız.

def basamak_toplami_tf(sayi):
    basamak_toplami = 0
    while sayi>0:
        basamak_toplami += sayi%10
        sayi = sayi // 10
    if basamak_toplami%2==0:
        print("Basamak toplamları çifttir.")
    else:
        print("Basamak toplamlari tektir.")
#basamak_toplami_tf(108)