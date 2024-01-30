import timeit
import random
import matplotlib.pyplot as plt
anzahlen=[]
zeiten=[]
x=0
while x < 10:
    def insertionSort(array):
        global start
        start=timeit.default_timer()
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        global stop
        stop=timeit.default_timer()
        zeit=stop-start
        anzahlen.append(län)
        zeiten.append(zeit)
        return anzahlen, zeiten
    x=x+1
    län=int(input("Wie lang soll die Liste sein:"))
    data =[random.randint(1,1000) for _ in range(län)]
    insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
plt.plot(anzahlen,zeiten)
plt.show()
print(anzahlen)
print(zeiten)
