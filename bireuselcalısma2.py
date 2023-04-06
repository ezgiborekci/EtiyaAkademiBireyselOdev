vize = int(input("Vize notunu gir: "))
final = int(input ("Final notu:"))
ortalamaNot =int(vize*0.4) + (final*0.6)

#final 40 tan kucukse kaldı
#ortalama 50 den küçükse kaldı
#vize finalin 2katı ise kaldı
#bunun dısında tüm durumlarda geçti


if final < 40:
    print("Kaldınız")
elif ortalamaNot < 50:
    print("Kaldınız")
elif vize == 2*final :
    print("Kaldınız")
else:
    print("Geçtiniz")
