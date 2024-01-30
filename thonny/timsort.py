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

# Beispielaufruf
mz=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
arr=[random.randint(1,mz) for _ in range(int(input("Wie lang soll die Liste sein:")))]
timsort(arr)
print(arr)

