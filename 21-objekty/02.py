class Auto:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def info(self):
        return f"{self.znacka} {self.model}"
    
auto1 = Auto("Tesla", "Model 5")
print(auto1.info())