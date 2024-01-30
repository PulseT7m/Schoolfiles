ln=int(input("gewünschte Länge der Liste: "))
liste=[]
from random import *
def rliste(l,liste):
    a=0
    while a<l:
        liste.append(randint(1,1000))
        a=a+1
    a=0
    for x in liste:
        print(liste[a])
        a=a+1
rliste(ln,liste)