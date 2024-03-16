#Sıcaklığı input olarak alınız. Her bir bakteri için optimaldir ve optimal değildir çıktılarını alacak
#programı yazınız. Termometrenin ölçüm aralığı -20 ile +100 arasındadır. Bu değerler dışında
#bir değer girildiğinde uyarı mesajı versin. Bakteriler ve optimal yaşama sıcaklıkları aşağıda
#verilmiştir.
#Streptococcus thermophilus: 40–45 °C
#Lactobacillus acidophilus: 35-38°C
#Escherichia Coli: 35-40°C

t = int(input("Sicakligi giriniz: "))
if not -20<t<100:
    print("Termometrenin olcebildigi aralik -20 ile 100 C araligidir. Tekrar giriniz.")
else:
    if 40 < t < 45:
        print("Streptococcus thermophilus icin optimal sicakliktir.")
    else:
        print("Streptococcus thermophilus icin optimal sicaklik degildir.")

    if 35 < t < 38:
        print("Lactobacillus acidophilus icin optimal sicakliktir")
    else:
        print("Lactobacillus acidophilus icin optimal sicaklik degildir.")

    if 35 < t < 40:
        print("Escherichia Coli icin optimal sicakliktir.")
    else:
        print("Escherichia Coli icin optimal sicaklik degildir.")