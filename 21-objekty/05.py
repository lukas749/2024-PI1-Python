class BankovyUcet:
    def __init__(self,saldo):
        self.__saldo = saldo

    def vloz(self,suma):
        if suma > 0:
            self.__saldo += suma

    def ziskaj_saldo(self):
        return self.__saldo
    
ucet = BankovyUcet(1000)
ucet.vloz(500)
print(ucet.ziskaj_saldo())