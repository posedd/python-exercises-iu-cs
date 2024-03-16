# Verilen bir metindeki en uzun kelimeyi bulan bir program yazın.
# Kelimeler boşluklarla ayrılır ve noktalama işaretleri yok sayılır.

text = input("Bir metin giriniz: ")
new_text=text.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").split()
kelime_sayisi = len(new_text)
en_uzun=(new_text[0])
for kelime in new_text:
    if len(kelime) >= len(en_uzun):
        en_uzun=kelime
print(f"En uzun kelime: {en_uzun}")