#string je reťazec znakov. "Ahoj" 
# reťazec začíname a končíme buď "" alebo '' - (pravý alt + P)
# \n - nový riadok, \t - tabulátor (odsadenie), \" - \" vypíše to text aj s úvodzovkami
# funkcia len() (lenght) - vráti dĺžku reťazca (vypíše počet znakov)
# znaky v reťazci sú indexované prvý znak má index 0
# index píšeme do hranatých zátvoriek [] (pravý alt + F, pravý alt + G)
retazec = "Ahoj Svet"
print (retazec)
print(len(retazec))
# print(retazec[0])
# for i in range(len(retazec)):
# print(retazec[i])
for znak in retazec: 
    print(znak)