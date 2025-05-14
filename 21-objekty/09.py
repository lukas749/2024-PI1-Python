class Animal:
    def speak(self):
        pass

class Pes:
    def speak(self):
        print("Haf!")

class Mačka:
    def speak(self):
        print("Mňau!")

pes = Pes()
mačka = Mačka()

mačka.speak()
pes.speak()
