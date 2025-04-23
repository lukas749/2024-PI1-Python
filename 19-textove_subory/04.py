# mena = open("mena.txt", "r", encoding="utf8")
# priezviska = open("priezviska.txt", "r", encoding="utf8")




# riadok1 = mena.readline()
# riadok2 = priezviska.readline()

# print(riadok1, riadok2)


# mena.close()
# priezviska.close()

fmena = open("mena.txt", "r", encoding="utf-8")
fpriezvisko = open("priezviska.txt", "r", encoding="utf-8")
fmena_priezviska = open("mena_priezviska.txt", "w", encoding="utf-8")

for meno in fmena:
    priezvisko = fpriezvisko.readline()
    print(f"{meno.strip()} {priezvisko.strip()}",file = fmena_priezviska )
fmena.close()
fpriezvisko.close()