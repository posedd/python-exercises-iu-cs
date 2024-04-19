# Word guessing game (Hangman)
import random

kelimeler = ["book","handbag", "meat", "romantic", "desire", "fortress", "banishment","taste", "cherry", "anatolia", "anatomy","persona"]
tahminler = []
kelime = random.choice(kelimeler)
can = 6

while can > 0:
    tahmin = input("Bir harf giriniz: ")
    tahminler.append(tahmin)

    if tahmin in kelime:
        print("Dogru tahmin!")
    else:
        print("Yanlis tahmin!")
        can -= 1
    acilan_kelime = ""
    for harf in kelime:
        if harf in tahminler:
            acilan_kelime += harf
        else:
            acilan_kelime += "_"

    print(f"Kelime: {acilan_kelime}")
    print(f"Kalan can: {can}")

    if not "_" in acilan_kelime:
        print("Kazandin!")
        break
    if can == 0:
        print(f"Tahmin hakkin bitti.\nKelime: {kelime}")
