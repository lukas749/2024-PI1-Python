pocet = 0
celková_suma = 0
for suma in 1.5, 10.2, 25.3, 4, 5.5, 100:
    pocet = pocet + 1
    celková_suma = celková_suma + suma
    print(f"Suma {pocet}. nákupu: {suma}€")
print(f"Celkový počet nákupov: {pocet}")
print(f"Celková suma nákupov je:{celková_suma}€")