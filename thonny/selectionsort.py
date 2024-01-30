#import timeit
import random
#import matplotlib.pyplot as plt
#anzahlen=[]
#zeiten=[]
x=0
while x < 10:
    def selectionSort(array, size):
        #global start
        #start=timeit.default_timer()
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
                (array[ind], array[min_index]) = (array[min_index], array[ind])             
        #global stop
        #stop=timeit.default_timer()
        #zeit=stop-start
        #anzahlen.append(län)
        #zeiten.append(zeit)
        #return anzahlen, zeiten
    x=x+1
    län=int(input("Wie lang soll die Liste sein:"))
    arr =[random.randint(1,1000) for _ in range(län)]
    size = len(arr)
#print(arr)
    selectionSort(arr, size)
#print('Die Liste nach dem sortieren lautet:')
print(arr)
#plt.plot(anzahlen,zeiten)
#plt.show()
#print(anzahlen)
#print(zeiten)