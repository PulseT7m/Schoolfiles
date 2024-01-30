def uebung1(zahl):
    if zahl <= zielzahl1:
        zahlen1.append(zahl*zahl)
        return uebung1(zahl+1)
zielzahl1=int(input("Nenne mir deine Zielzahl. "))
startzahl=1
zahlen1=[]
uebung1(startzahl)
print(zahlen1)

def uebung2(zahl):
    if zahl <= zielzahl2:
        if zahl%2==0:
            zahlen2.append(zahl)
        return uebung2(zahl+1)
zielzahl2=int(input("Nenne mir deine Zielzahl. "))
zahlen2=[]
uebung2(startzahl)
print(zahlen2)

class Katze:
    def __init__(self,name,alter,kinder):
        self.name=name
        self.alter=alter
        self.kinder=kinder
    def miau(self):
        print(f"{self.name}: Miau")
katze1=Katze("Simba",10,2)
katze1.miau()
