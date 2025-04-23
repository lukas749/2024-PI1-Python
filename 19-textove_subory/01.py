subor = open("subor.txt", "r") #relatívna cesta k súboru (musí byť v tom istom priečinku ako samotný kód)
# otvorí súbor subor.txt na čítanie, pre zápis miesto "r" použijeme "w", "r" = read, "w" = write. Ak súbor neexistuje vypíše chybu
# subor = open("c:/dokumenty/subor.txt", "r") - toto je absolútna cesta ) "c:/dokumenty/subor.txt"
# subor = open("../subor.txt", "r") .. je o priečinok vyššie 

# for i in range(4):
#     riadok = subor.readline() #readline prečíta celý riadok (od miesta kde sa aktuálne nachádza) zo súboru a uloží do premennej riadok
#     print(riadok)

# riadok = subor.readline()
# while riadok !="":
#     print(riadok)
#     riadok = subor.readline()

while True:
    riadok = subor.readline()
    if riadok =="":
            break # break preruší cyklus a vyskočí z neho
    print(riadok.strip()) # strip odstráni nečitateľné znaky napr.: enter, \n, \t


subor.close() # zatvorí súbor
