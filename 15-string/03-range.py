# range() - je funkcia ktorá generuje nejakú postupnos
# range(5) - postupnosť 0,1,2,3,4
# range(od,pokiaľ-1, krok)
# range môže mať aj klesajúcu postupnosť
print(list(range(5)))
print(list(range(2,5)))
print(list(range(2,10,2)))
print(list(range(5,0,-1)))

ret = "Ahoj"
for i in range(len(ret)-1,-1, -1):
    print(ret[i])