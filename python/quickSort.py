def quickSort(a):
    size = len(a)
    if size > 1:
        pivotIndex = partition(a)
        a[0:pivotIndex] = quickSort(a[0:pivotIndex])
        a[pivotIndex+1:size] = quickSort(a[pivotIndex+1:size])
    return a

def partition(a):
    pivot = a[0]
    size = len(a)
    pivotIndex = 0
    for index in range(1, size):
        if a[index] < pivot:
            pivotIndex += 1
            a[index], a[pivotIndex] = a[pivotIndex], a[index]
    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex    

print(quickSort([23,10,12,20,25,13,15,22]))