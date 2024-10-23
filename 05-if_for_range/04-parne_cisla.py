cislo = int(input("Zadaj číslo:"))

# vypis nepárnych čísel
print(f"Nepárne čísla do {cislo}:")
for i in range(1, cislo+1 ,2):
    print(i)

# vypis parnych cisiel
print(f"Párne čísla do {cislo}:")
for i in range(2, cislo+1 ,2):
    print(i)
if cislo % 2 == 0:
    print(f"Číslo {cislo} je párne.")
else:
    print("Číslo je nepárne.")