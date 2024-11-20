import random # knižnica, ktorá slúži na generovanie náhodných hodnôt

nahodne_cislo = random.randint(1,10) # vygeneruje náhodné celé číslo v rozsahu 1-10
print(nahodne_cislo)

nahodna_farba = random.choice(["red", "green", "blue","yellow","cyan","black"]) # vygeneruje náhodnú hodnotu zo zoznamu hodnôt, zoznam ohraničíme alt+f, alt+g, []
print(nahodna_farba)

nahodne_pismeno = random.choice("aeiouy") # vygeneruje náhodnú samohlásku
print(nahodne_pismeno)