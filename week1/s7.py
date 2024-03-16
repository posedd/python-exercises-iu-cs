#Aynı noktadan ters yönlerde harekete geçen iki aracın gittiği mesafeleri input olarak
#giriniz. (Doğu: negatif, Batı: pozitif olacak şekilde) Program hangi aracın daha fazla mesafe
#gittiğini versin.

b = float(input("Batida gidilen mesafeyi giriniz: "))
d = float(input("Dooguda gidilen mesfeyi gir lan it: "))
if b+(-d)<0:
    print(f"Doguda {d-b} kadar yol gitti")
elif b+(-d)>0:
    print(f"Batida {b-d} kadar yol gitti")
else:
    print("Esit")





