#rekursiver Algorithmus zur Berechnung von Summe bis n
def summe(n):
    if n == 0:
        return 0
    else:
        return n + summe(n-1)
n=int(input("Bis zu welcher Zahl soll die Summe gebildet werden? "))
print(f"Die Summe aller Zahlen von 0 bis {n} beträgt {summe(n)}.")

#rekursiver Algorithmus zur Berechnung von Fakultät n
def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n-1)
n=int(input("Die Fakultät welcher Zahl soll gebildet werden? "))
print(f"Die Fakultät der Zahl {n} beträgt {fak(n)}.")

#rekursiver Algorithmus zur Berechnung von Fibonacci-Folge bis Stelle n
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n=int(input("Die Fibonacci-Folge bis zu welcher Zahl soll gebildet werden? "))
print(f"Die Fibonacci-Folge bis zur Zahl {n} beträgt {fib(n)}.")

#rekursiver Algorithmus zur Zinsrechnung
zins=int(input("Wie lautet der Jahreszins in Prozent? "))
z=zins/100+1
g=int(input("Wieviel Geld wird am Anfang eingezahlt? "))
j=int(input("Wieviel Jahre soll das Geld drinnen bleiben? "))
def zr(g,j):
    if j <= 0:
        return g
    else:
        return zr(g,j-1)*z
print(f"Mit einem Startguthaben von {g}€ und einem Jahreszins von {zins}% beträgt nach {j} Jahren das Guthaben {zr(g,j)}€.")




































