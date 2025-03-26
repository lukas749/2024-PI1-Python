while True:
    print("[1] pre zasifrovanie")
    print("[2] pre rozsifrovanie")
    print("[3] pre ukoncenie")

    choise = input("Vyber cislo: ")
    text2 = ""

    if choise == "1":
        text = input("Zadaj text: ")
        text = text.lower()
        for i in text:
            char = ord(i)+1
            if char == 123:
                char = 97
            text2 += chr(char)
        print("Zasifrovany text: ",text2)
        print("----------------")

    elif choise == "2":
        text = input("Zadaj text: ")
        text = text.lower()
        for i in text:
            char = ord(i)-1
            if char == 96:
                char = 122
            text2 += chr(char)
        print("Rozsifrovany text:",text2)
        print("----------------")
        
    elif choise == "3":
        break
    else:
        print("musis vybrat cislo: 1,2,3")
        print("----------------")