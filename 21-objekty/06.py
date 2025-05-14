class Zviera:
    def zvuk(self):
        pass
class Kocur:
    def zvuk(self):
        print("Mňau!")

class Pes:
    def zvuk(self):
        print("Haf!")

zviera1 = Kocur()
zviera2 = Pes()

for zviera in [zviera1, zviera2]:
    zviera.zvuk()
