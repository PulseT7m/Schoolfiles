import random
def mergesort(arr):
    if len(arr)>1:
        #r=mitte der liste; punkt an dem sie geteilt wird
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]
        #beide hälften sortieren
        mergesort(L)
        mergesort(M)
        i=j=k=0
        #bis ende einer der beiden hälften erreicht wird: größere zahl wählen und an richtige stelle in sortierter Liste einfügen
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=M[j]
                j=j+1
            k=k+1
        #sobald keine elemente mehr in einer der beiden listen übrig sind fügen wir den rest in die sortierte liste ein
        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j<len(M):
            arr[k]=M[j]
            j=j+1
            k=k+1

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
mz=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
arr=[random.randint(1,mz) for _ in range(int(input("Wie lang soll die Liste sein:")))]
mergesort(arr)
print("Die sortierte Liste lautet: ")
#printlist(arr)
print(arr)