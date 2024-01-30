###OOP-->objektorientierte Programmierung
#Was sind Objekte?
#methoden=funktionen die nur innerhalb einer klasse gelten

###Eigene Klasse definieren###
class Hund: #Klassen immer mit Großbuchstaben beginnen, mehrere Wörter: neues Wort immer groß(NeuerHund)
    #Attribute
    def __init__(self, name): #Init-Methode wird beim Anlegen eines Objekts ausgeführt(Konstruktor)
        self.name=name
    #Methode
    def bellen(self):
        print("Wau Wau")        
hund1=Hund("Siegfried")#eine instanz der klasse hund erzeugen ->objekt
print(type(hund1))
hund1.bellen()
print(hund1.name)
