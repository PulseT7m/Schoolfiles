#1
a=int(input("zahl 1:"))
b=int(input("zahl 2:"))
def addieren(a,b):
    return a+b
addieren(a,b)
print(addieren(a,b))

#2
from random import *
def drucke_zufallszahl():
    print(randint(1,100))
drucke_zufallszahl()

#3
liste=[]
x=0
def zufallsliste(x,liste):
    while x<100:
        liste.append(randint(1,6))
        x=x+1
    return liste
zufallsliste(x,liste)
print(liste)
print(len(liste))