print("Zisti, či je súčet dvoch posledných cifier párny.")

num = str(input("Zadaj číslo: "))

if len(num) < 2:
    print("Číslo je jednociferné.")
    exit()

x = int(num[-1])
y = int(num[-2])
z = x + y

if z%2 == 0:
  str = "párne."
else:
  str = "nepárne."

print("Súčet dvoch posledných cifier je",z,"toto číslo je",str)
