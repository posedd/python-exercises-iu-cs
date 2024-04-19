# Moleküler biyoloji ve biyokimyada tamamlayıcılık, veya komplementerlik, iki
# molekülün birbiriyle temas ettikleri yüzeylerindeki şekillerin uyumu sayesinde birbirlerine
# sıkı bir şekilde bağlanarak bir bütün oluşturma özellikleridir. Buna göre A ile T ve G ile C
# birbirinin tamamlayıcısıdır. Örneğin A G T C A T G dizisinin tamamlayıcısı T C A G T A
# C bu bilgilere dayanarak verilen bir DNA dizisinin tamamlayıcısını bulup liste olarak
# veren fonksiyon yazınız.

def dna_tamlama(dizi):
    tamlayici = []
    for nukleotid in dizi:
        if nukleotid == "A":
            tamlayici.append("T")
        elif nukleotid == "T":
            tamlayici.append("A")
        elif nukleotid == "C":
            tamlayici.append("G")
        elif nukleotid == "G":
            tamlayici.append("C")
    return tamlayici
print(dna_tamlama("A G T C A T G"))