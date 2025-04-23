subor = open("subor2.txt", "w") # otvorí súbor na zápis, ak súbor neexistuje tak sa vytvorí, ak súbor existuje, tak sa zmaže celý obsah
# subor.write("Ahoj\n")
# subor.write("ako\n")
# subor.write("sa\n")
# subor.write("mas?\n")
print("Ahoj", file=subor)
print("ako", file=subor)
print("sa", file=subor)
print("mas?", file=subor)



subor.close()