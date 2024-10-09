n = int(input("Zadaj n:"))
faktorial = 1
for i in range(n):
    faktorial = faktorial * (i+1) # sucet + (i+1) je výraz , najskôr sa vypočíta výraz a výsledná hodnota sa priradí do premennej sucet
    # print(i, i+1, sucet)
# print("Faktorial prvých", n , "čísel je:", faktorial)
# print(n, "!=",faktorial)
print(f"{n}! = {faktorial}") # {} napíšeme Alt Gr + B, Alt Gr + N 