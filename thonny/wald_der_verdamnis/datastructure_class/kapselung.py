class Konto():
    def __init__(self,guthaben,pin):
        self.__pin=pin
        self.__guthaben=guthaben
    def get_guthaben(self,pin):
        if pin==self.__pin:
            return self.__guthaben
    def set_guthaben(self,pin,wert):
        if pin==self.__pin:
            self.__guthaben=wert

konto1=Konto(5000)
konto1.set_guthaben(10000)
print(konto1.get_guthaben())
