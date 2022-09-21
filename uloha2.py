print("Naprogramuj funkciu, ktorá zistí, či dané číslo x patrí do intervalu <a,b>.")

a = int(input("Zadaj začiatočnú hodnotu intervalu, a: "))
b = int(input("Zadaj konečnú hodnotu intervalu, b: "))

x = int(input("Zadaj premennú x: "))

if a <= x <= b:
    print("Číslo",x,"patrí do intervalu.")
else:
    print("Číslo",x,"nepatrí do intervalu.")
