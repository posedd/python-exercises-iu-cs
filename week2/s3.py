# İki farklı organizmanın DNA dizilerini karşılaştırarak benzerliklerini bulan bir program yazın.
# DNA dizileri, dizilmiş nükleotidlerden oluşur: adenin (A), timin (T), sitozin (C) ve guanin (G).
# Verilen iki DNA dizisinin herhangi bir konumdaki karakterleri karşılaştırılır ve eşleşme sayısı hesaplanır.
# Örneğin:
# Dizgi 1: "ATCGATCGATCG"
# Dizgi 2: "ATCGATAGCTAG"

dna1 = ("ATCGATCGATCG")
dna2 = ("ATCGATAGCTAG")
dna_uzunluk = len(dna1) or len(dna2)
eslesme = 0
print(dna_uzunluk)
for i in range(dna_uzunluk):
    if dna1[i] == dna2[i]:
        eslesme += 1
benzerlik = eslesme/dna_uzunluk*100
print(f"Benzerlik orani: %{benzerlik}")