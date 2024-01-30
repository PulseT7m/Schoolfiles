import random
län=int(input("Wie lang soll die Liste sein:"))#random.randint(1,10000)
arr=[random.randint(1,10) for _ in range(län)]		#fill array
# print(arr)		#print unsorted as array 
def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] < arr[i + 1]:
            arr[i],arr[i+1]=arr[i],arr[i+1]
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i-=1
BubbleSort(arr)
print(arr)