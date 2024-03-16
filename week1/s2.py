#Kullanıcıdan 3 farklı sayı girmesini isteyen ve bu sayıların en büyüğünü ekrana
#yazdıran bir program yazınız.

a = int(input("ilk tam sayiyi giriniz: "))
b = int(input("ikinci tam saiyiy gir: "))
c = int(input("ucuncu tam sayiyi gir: "))

#a'yı max sec ve karsilastir.

if a == b and b==c:
    print("Tum sayilar esit")
elif  a < b:
    a=b
elif a < c:
    a=c
print(a)


