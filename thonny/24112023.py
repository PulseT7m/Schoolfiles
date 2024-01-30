# 1. man teilt ein hauptproblem in mehrere kleinere teilprobleme, solange bis diese ganz simpel zu lösen sind
# erst teilt man es rekursiv bis sie ganz simpel zu lösen sind und dann fügt man alles zusammen
# 2.a: bei einem iterativen lösungsansatz wird ein problem mithilfe von schleifen gelöst
# bei einem rekursiven lösungsansatz wird ein problem mithilfe des sich selbst aufrufens einer funktion gelöst, es wird eine endbedingung benötigt
# b:
b=int(input("was soll die basis deiner Potenz sein? "))
e=int(input("was soll der exponent deiner Potenz sein? "))
d=b
def p1(b,e):
    b=d
    if e==0:
        return 1
    else:
        for _ in range(1,e):
            b=b*d
        return b     
print(p1(b,e))

def p2(b,e):
    if e < 1:
        return 1
    else:
        return b*p2(b,e-1)
    print(b)
print(p2(b,e))


links=[2,3,6,8]
rechts=[1,3,5,7]
sortiert=[]
def merge(l,r,liste):
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            liste.append(l[i])
            i+=1
        else:
            liste.append(r[j])
            j+=1
    while i<len(l):
        liste.append(l[i])
        i+=1
    while j<len(r):
        liste.append(r[j])
        j+=1

def p(liste):
    for _ in range(len(liste)):
        print(liste[_], end=" ")
        
merge(links,rechts,sortiert)
p(sortiert)

















