class Banka:
    def balance(self, balance = 0):
        self.__balance = balance

    def vklad(self,množstvo):
        self.__balance += množstvo
        print(f"Vložená čiastka: {množstvo}, aktuálny stav účtu: {self.__balance}")

    def výber(self,množstvo):
        if množstvo > self.__balance:
            print("Nedostatok peňazí na výber z účtu")
        else:
            self.__balance -= množstvo
            print(f"Vybratá čiastka: {množstvo}, aktuálny stav účtu: {self.__balance}")

účet = Banka(1000)
účet.vklad = (500)
účet.výber = (300)

účet.vklad(300)