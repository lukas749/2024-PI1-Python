# print(bin(255)) # vypíše nám číslo v binárnej sústave
# print(hex(255)) # vypíše nám číslo v hexadecimálnej sústave
# print(0b11111111) # vypíše binárne číslo v desiatkovej podobe
# print(0xFF) # vypíše nám hexadecimálne číslo v desiatkovej podobe

def dec_bin(cislo):
     binarne = ""
     while cislo > 0:
         zvysok = cislo % 2
         binarne = str(zvysok) + binarne
         print(binarne)
         cislo = cislo // 2
     return binarne

def dec_hex(cislo):
    binarne = ""
    while cislo > 0:
        zvysok = cislo % 16
        # if zvysok == 10:
        #     zvysok = "A"
        # if zvysok == 11:
        #     zvysok = "B"
        # if zvysok == 12:
        #     zvysok = "C"
        # if zvysok == 13:
        #     zvysok = "D"
        # if zvysok == 14:
        #     zvysok = "E"
        # if zvysok == 15:
        #     zvysok = "F"
        if zvysok < 10:       
            binarne = str(zvysok) + binarne
        else: 
            binarne = chr(55+ zvysok) + binarne
        
        
        print(binarne)
        

        cislo = cislo // 16
    return binarne

def dec_oct(cislo):
        binarne = ""
        while cislo > 0:
            zvysok = cislo % 8
            binarne = str(zvysok) + binarne 
            print(binarne)
            cislo = cislo // 8
        return binarne

print("Zadaj 1 pre prevedenie čísla do binárnej sústavy")
print("Zadaj 2 pre prevedenie čísla do hexadecimálnej sústavy")
print("Zadaj 3 pre prevedenie čísla do osmičkovej sústavy")

choise = input("Vyber si číslo:")
cislo = int(input("Zadaj číslo na prevedenie:"))

if choise == 1:
    print(dec_bin(cislo))
if choise == 2:
    print(dec_hex(cislo))
if choise == 3:
    print(dec_oct(cislo))



 