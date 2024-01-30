import random
län=int(input("Wie lang soll die Liste sein:"))#random.randint(1,10000)
arr=[random.randint(1,1000) for _ in range(län)]		#fill array
def lk_sort2(arr):
    i=0
    l=len(arr)
    while i < l-1:
        if arr[i]>=arr[i+1] and i==0:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=1
        elif i==0 or arr[i]<=arr[i+1]:
            i+=1
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i-=1
lk_sort2(arr)
print(arr)