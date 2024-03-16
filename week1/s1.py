#: Kullanıcıdan üç kenar uzunluğunu girmesini isteyen ve bu uzunlukların bir üçgen
#belirtip belirtmediğini gösteren, belirtiyor ise üçgenin türünü belirleyen bir program yazınız.
#Üçgen kuralı: a,b,c kenar uzunlukları olmak üzere: “a+b > c ve a+c > b ve b+c > a” koşulu
#sağlanmalı

a = int(input("Ucgenin birinci kenarini giriniz: "))
b = int(input("Ucgenin ikinci kenarini giriniz: "))
c = int(input("Ucgenin ucuncu kenarini giriniz: "))

if a+b <= c or a+c <= b or b+c <= a :
    print("Ucgen belirtmez.")
elif a==b==c:
    print("Eskenar ucgendir.")
elif a == b or b == c or a == c:
    print("Ucgen ikizkenardir")
elif a**2+b**2==c**2 or b**2+c**2==a**2  or a**2+c**2==b**2:
    print("dik ucgendir.")
else:
    print("Cesitkenardir.")




