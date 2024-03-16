#Sizden istenilen ondalıklı sayının kesirli ifadesini bulunuz ve bu sayının 1/10 birimlik
#aralıkta hangi iki kesir arasında olduğunu belirleyiniz.

from fractions import Fraction
from decimal import Decimal

ondalik = Decimal(input("Ondalikli giriniz: "))
ondalik_arti = (ondalik + Decimal(0.01))
ondalik_eksi = (ondalik - Decimal(0.01))

kesir = Fraction(ondalik).limit_denominator(1000)

print(f"Girilen ondalikli sayinin kesirli ifadesi = {kesir}")
#print(f"{ondalik:.16f}")

kesir_arti = Fraction(ondalik_arti).limit_denominator(1000)
kesir_eksi = Fraction(ondalik_eksi).limit_denominator(1000)

print(f"Girilen ondalikli sayi {kesir} kesirli sayisina esittir ve {kesir_eksi} , {kesir_arti} kesirli sayilari arasindadir.")
print(f"{kesir_eksi} < {kesir} < {kesir_arti}")