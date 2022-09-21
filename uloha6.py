print("Funkcia, ktorá zistí, či je dané číslo párne.")
num = int(input("Zadaj číslo: "))

if num == 0:
  print("Číslo musí byť väčšie ako nula.")
elif num%2 == 0:
  print("Číslo je párne.")
else:
  print("Číslo je nepárne.")
