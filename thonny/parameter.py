#1
a=int(input("zahl 1:"))
b=int(input("zahl 2:"))
def addieren(a,b):
    return a+b
addieren(a,b)
print(addieren(a,b))

#2
liste=[]
element=[input("Gebe mir ein Element: ")]
def erweiterte_liste(liste,element):
    liste.append(element[0])
erweiterte_liste(liste,element)
print(liste)

#3
a=[int(input("zahl 1:"))]
b=[int(input("zahl 2:"))]
def vertausche(a,b):
    a.append(b[0])
    b.append(a[0])
vertausche(a,b)
print(a[1])
print(b[1])

a=int(input("zahl 1:"))
b=int(input("zahl 2:"))
def vertausche(a,b):
    c=a
    a=b
    b=c
    return a,b
print(vertausche(a,b))

a,b=b,a
print(a)
print(b)
