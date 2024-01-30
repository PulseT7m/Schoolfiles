import random
def quicksort(arr):
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
# Beispielaufruf
mz=int(input("Was soll die größtmögliche Zahl deiner Liste sein? "))
arr=[random.randint(1,mz) for _ in range(int(input("Wie lang soll die Liste sein:")))]
sorted_arr = quicksort(arr)
print(sorted_arr)