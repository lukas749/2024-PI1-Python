# slice sú tzv. rezy reťazca, ak potrebujeme vybrať z reťazca nejakú časť
ret = "Ahoj Svet"
print(ret[0:4]) # vypíše znaky od 0 do 4-1 = 3
print(ret[:4]) # keď nie je zadaná hodnota program si myslí že pred : je 0
print(ret[5:10])
print(ret[5:]) # keď nie je zadaná hodnota za : program si myslí že za : je konečné číslo (v tomto prípade 10)
print(ret[-1]) # program pôjde spätne (začne od písmena t)
print(ret[1:-1])
print(ret[::-1])