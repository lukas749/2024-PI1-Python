class Car:
    def __init__ (self, model, rok):
        self.model = model
        self.rok = rok

    def info(self):
        print(f"Model auta je: {self.model}, rok výroby auta je : {self.rok}")

auto1 = Car("Audi", 2020)

auto1.info()