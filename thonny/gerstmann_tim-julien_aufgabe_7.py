def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def lk_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    lk_sort(array, low, pi - 1)
    lk_sort(array, pi + 1, high)
    print("Schritt beendet")
def printdata(arr):
    for _ in range(len(arr)):
        print(arr[_],end=" ")
    print("")

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsortiertes Array")
printdata(data)

size = len(data)

lk_sort(data, 0, size - 1)

print('Sortiertes Array in aufsteigender Reihenfolge:')
printdata(data)
