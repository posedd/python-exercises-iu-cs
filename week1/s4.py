#Bir kıyafete verilen fiyata göre, indirim yapılıp yapılmayacağını belirleyen ve
#yapılacak ise indirimli fiyatı gösteren bir program yazınız. İndirim oranı ve indirim eşiği keyfi
#sayılardır.
fiyat = int(input("Kiyafet fiyatini giriniz: "))
ind_orani = 20;
indirimli_fiyat = fiyat - fiyat*ind_orani/100
if fiyat <= 300:
    print(f"Urunde indirim yoktur. {fiyat}")
else:
    print(f"Urunun indirimli fiyati = {indirimli_fiyat}")



