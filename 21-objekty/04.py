class Zviera:
    def zvuk(self):
        print("Zviera vydáva zvuk.")

class Pes(Zviera):
    def zvuk(self):
        print("Haf!")

pes = Pes()

pes.zvuk()