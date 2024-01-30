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
    print()
        
merge(links,rechts,sortiert)
p(sortiert)

def m(l,r,liste):
    il=ir=0
    while True:
        if il == len(l):
            liste.append(r[-1])
            break
        elif ir == len(r):
            liste.append(l[-1])
            break
        if l[il]>r[ir]:
            liste.append(r[ir])
            ir+=1
        elif l[il]>r[ir]:
            liste.append(l[il])
            il+=1
        else:
            liste.append(l[il])
            liste.append(r[ir])
            il+=1
            ir+=1
    return liste

#m(links,rechts,sortiert)
#p(sortiert)
