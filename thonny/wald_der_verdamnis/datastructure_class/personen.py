
class Person:
    def __init__(self,vorname,nachname,alter,wohnort):
        self.vorname=vorname
        self.nachname=nachname
        self.alter=alter
        self.wohnort=wohnort
    def vorstellen(self):
        print(f"Ich heiße {self.vorname} {self.nachname}, bin {self.alter} Jahre alt und wohne in {self.wohnort}.")
person1=Person("Ralf","Rolf",-100,"Frankfurt")
person1.vorstellen()