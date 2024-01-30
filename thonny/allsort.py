import timeit
import random
import matplotlib.pyplot as plt
anzahlenb=[]
zeitenb=[]
# länb=int(input("Wie lang soll die Liste sein:"))#random.randint(1,10000)
# arrb=[random.randint(1,10000) for _ in range(länb)]
def BubbleSort(arr):
    global startb
    startb=timeit.default_timer()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    global stopb
    stopb=timeit.default_timer()
    zeitb=stopb-startb
    anzahlenb.append(länb)
    zeitenb.append(zeitb)
    return anzahlenb, zeitenb
#BubbleSort(arrb)
#plt.plot(anzahlenb,zeitenb)
#plt.show()
#print(anzahlenb)
#print(zeitenb)

anzahlens=[]
zeitens=[]
def selectionSort(array, size):
    global starts
    starts=timeit.default_timer()
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
                (array[ind], array[min_index]) = (array[min_index], array[ind])
    global stops
    stops=timeit.default_timer()
    zeits=stops-starts
    anzahlens.append(läns)
    zeitens.append(zeits)
    return anzahlens, zeitens
# läns=int(input("Wie lang soll die Liste sein:"))
# arrs =[random.randint(1,10000) for _ in range(läns)]
# sizes = len(arrs)
#selectionSort(arrs, sizes)
#print('Die Liste nach dem sortieren lautet:')
#print(arrs)
#plt.plot(anzahlens,zeitens)
#plt.show()
#print(anzahlens)
#print(zeitens)


anzahleni=[]
zeiteni=[]
def insertionSort(array):
    global starti
    starti=timeit.default_timer()
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    global stopi
    stopi=timeit.default_timer()
    zeiti=stopi-starti
    anzahleni.append(läni)
    zeiteni.append(zeiti)
    return anzahleni, zeiteni
# läni=int(input("Wie lang soll die Liste sein:"))
# datai =[random.randint(1,10000) for _ in range(läni)]
# insertionSort(datai)
# print('Sorted Array in Ascending Order:')
# print(datai)
#plt.plot(anzahleni,zeiteni)
#plt.show()
# print(anzahleni)
# print(zeiteni)


anzahlenm=[]
zeitenm=[]
def mergesort(arr):
    global startm
    startm=timeit.default_timer()
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
    global stopm
    stopm=timeit.default_timer()
    zeitm=stopm-startm
    anzahlenm.append(mzm)
    zeitenm.append(zeitm)
    return anzahlenm, zeitenm
# mzm=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
# arrm=[random.randint(1,mzm) for _ in range(int(input("Wie lang soll die Liste sein:")))]
# mergesort(arrm)
#plt.plot(anzahlenm,zeitenm)
#plt.show()


anzahlenq=[]
zeitenq=[]
def quicksort(arr):
    global startq
    startq=timeit.default_timer()
    # Basisfall: Wenn die Eingabeliste leer oder nur ein Element lang ist, ist sie bereits sortiert
    if len(arr) <= 1:
        return arr
    else:
        # Der erste Element wird als Pivot gewählt
        pivot = arr[0]
        # Teilt die Liste in Elemente, die kleiner oder gleich dem Pivot sind
        less = [x for x in arr[1:] if x <= pivot]
        # Und in Elemente, die größer als der Pivot sind
        greater = [x for x in arr[1:] if x > pivot]
        # Ruft die Funktion rekursiv für die kleineren und größeren Elemente auf und fügt sie mit dem Pivot zusammen
        return quicksort(less) + [pivot] + quicksort(greater)
    global stopq
    stopq=timeit.default_timer()
    zeitq=stopq-startq
    anzahlenq.append(mzq)
    zeitenq.append(zeitq)
    return anzahlenq, zeitenq

# mzq=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
# arrq=[random.randint(1,mzq) for _ in range(int(input("Wie lang soll die Liste sein:")))]
# sorted_arr = quicksort(arrq)



anzahlent=[]
zeitent=[]
import random
def insertion_sort(arr, left=0, right=None):
    # Implementierung des Einfügesortieralgorithmus, um Teillisten mit einer bestimmten Länge zu sortieren
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    # Implementierung des Verschmelzungsschritts für den Timsort
    len_left = mid - left + 1
    len_right = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def timsort(arr):
    global startt
    startt=timeit.default_timer()
    # Implementierung des Timsort-Algorithmus
    min_run = 32
    n = len(arr)

    # Anwenden des Einfügesortieralgorithmus auf Teilbereiche der Eingabeliste
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        # Verschmelzung der sortierten Teilbereiche, um eine sortierte Gesamtliste zu erhalten
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min(n - 1, start + size * 2 - 1)

            merge(arr, start, mid, end)

        size *= 2
    global stopt
    stopt=timeit.default_timer()
    zeitt=stopm-startt
    anzahlent.append(mzt)
    zeitent.append(zeitt)
    return anzahlent, zeitent

# Beispielaufruf
# mzt=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
# arrt=[random.randint(1,mzt) for _ in range(int(input("Wie lang soll die Liste sein:")))]
# timsort(arrt)

länb=1000#int(input("Wie lang soll die Liste sein:"))#random.randint(1,10000)
arrb=[random.randint(1,10000) for _ in range(länb)]
läns=1000#int(input("Wie lang soll die Liste sein:"))
arrs =[random.randint(1,10000) for _ in range(läns)]
sizes = len(arrs)
läni=1000#int(input("Wie lang soll die Liste sein:"))
datai =[random.randint(1,10000) for _ in range(läni)]
mzm=10000#int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
länm=1000#int(input("Wie lang soll die Liste sein:"))
arrm=[random.randint(1,mzm) for _ in range(länm)]
mzq=10000#int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
länq=1000#int(input("Wie lang soll die Liste sein:"))
arrq=[random.randint(1,mzq) for _ in range(länq)]
mzt=10000#int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
länt=1000#int(input("Wie lang soll die Liste sein:"))
arrt=[random.randint(1,mzt) for _ in range(länt)]
    
for i in range(10):
    länb+=500
    arrb=[random.randint(1,10000) for _ in range(länb)]
    läns+=500
    arrs =[random.randint(1,10000) for _ in range(läns)]
    sizes = len(arrs)
    läni+=500
    datai =[random.randint(1,10000) for _ in range(läni)]
    länm+=25000
    arrm=[random.randint(1,mzm) for _ in range(länm)]
    länq+=25000
    arrq=[random.randint(1,mzq) for _ in range(länq)]
    länt+=1000000
    arrt=[random.randint(1,mzt) for _ in range(länt)]
    BubbleSort(arrb)
    selectionSort(arrs, sizes)
    insertionSort(datai)
    mergesort(arrm)
    sorted_arr = quicksort(arrq)
    timsort(arrt)
    print(i)


print("baguette")
plt.plot(anzahlenb,zeitenb,"-b",anzahlens,zeitens,"-r",anzahleni,zeiteni,"-g",anzahlenm,zeitenm,"-m",anzahlenq,zeitenq,"-k",anzahlent,zeitent,"-y")
plt.show()
#
plt.plot(anzahlenb,zeitenb,"-b")
plt.show()
plt.plot(anzahlens,zeitens,"-r")
plt.show()
plt.plot(anzahleni,zeiteni,"-g")
plt.show()
plt.plot(anzahlenm,zeitenm,"-m")
plt.show()
plt.plot(anzahlenq,zeitenq,"-k")
plt.show()
plt.plot(anzahlent,zeitent,"-y")
plt.show()
print("baguette")