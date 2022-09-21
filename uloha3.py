print("Program, ktorý vráti prevrátenú hodnotu daného čísla")

x = input("Zadaj číslo: ")

if x == '0':
  print("Nulou sa nedá deliť")
else:
  vysledok = 1/int(x)
  print("Prevrátená hodnota čísla: ", vysledok)
