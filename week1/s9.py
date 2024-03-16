#Girilen sayının 6’ya bölünüp bölünmediğini ekrana yazdıran programı yazınız
x = int(input("Tam sayi giriniz: "))
if x%2==0 and x%3==0:
    print("sayi 6'ya tam bolunur.")
else:
    print("Sayi 6'ya bolunmez")