print("Naprogramuj funkciu, ktorá po zadaní troch hodnôt vypíše, "
      "či hodnoty sú stranami trojuholníka a ak áno, tak akého (pravouhlého, rovnoramenného, rovnostranného ap.)")

a = int(input("Strana a = "))
b = int(input("Strana b = "))
c = int(input("Strana c = "))

if a+b>c and b+c>a and a+c>b:
    if a == b == c:
        print("Trojuholník je rovnostranný.")
    elif a==b or b==c or a==c:
        print("Trojuholník je rovnoramenný.")
    elif a**2 == (b**2+c**2) or b**2 == (a**2+c**2) or c**2 == (a**2+b**2):
        print("Trojuholník je pravouhlý.")
    else:
        print("Trojuholník je rôznostranný.")
else:
    print("Strany nepatria trojuholníku.")
