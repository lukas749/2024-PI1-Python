class Osoba:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def __str__(self):
        return f"{self.meno} má {self.vek} rokov."
    
osoba1 = Osoba("Janko", 30)
print(osoba1)