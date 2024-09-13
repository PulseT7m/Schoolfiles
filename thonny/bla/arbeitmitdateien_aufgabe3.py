#das 100 zufällige, 8-stellige Binärzahlen (bestehend aus 0 und 1) generiert und in eine Textdatei namens "binaerzahlen.txt" schreibt. Jede Zahl soll in einer neuen Zeile stehen.
import random as r
with open("binaerzahlenn.txt","w") as file:
    file.write("")
    
for i in range(0,99):
    with open("binaerzahlenn.txt","a") as file:
        file.write(f"\n {r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}{r.randint(0,1)}")
        
with open("binaerzahlenn.txt","r") as file:
    inhalt = file.read()
print(inhalt)