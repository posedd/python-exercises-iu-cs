#Programdaki hatayı bulup açıklayarak hatayı düzeltiniz.

sayi1 = float(input("Birinci sayiyi giriniz."))
sayi2 = float(input("Ikinci sayiyi giriniz."))

if sayi1 == sayi2:
    fark = abs(sayi1-sayi2)

    if fark < 0.1:
        print("iki sayi birbirine esit degil")
    else:
        print("iki sayi birbirine esit degil")
else:
    print("iki sayi birbirine esit degil")