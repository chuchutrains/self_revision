def merge(arrayA, arrayB):
    arrayC = []
    sizeA = len(arrayA)
    sizeB = len(arrayB)
    indexA = indexB = 0

    # Sort based on smallest.
    while indexA < sizeA and indexB < sizeB:
        if arrayA[indexA] < arrayB[indexB]:
            arrayC.append(arrayA[indexA])
            indexA = indexA + 1
        else:
            arrayC.append(arrayB[indexB])
            indexB = indexB + 1

    # Sort the remaining.
    for i in range(indexA, sizeA):
        arrayC.append(arrayA[i])
    for i in range(indexB, sizeB):
        arrayC.append(arrayB[i])

    return arrayC  

def mergeSort(array):
    size = len(array)
    #  'is' operator check if both operands are referring to the same object
    if size == 1: return array
    
    midIndex = int(size/2)
    # Eg midIndex is 4, firstHalf will be [27,10,12,20].
    firstHalf  = array[0:midIndex]
    # Start the array with midIndex, which is array[4].
    secondHalf = array[midIndex:size]

    # Self-loop continue to break into half the array.
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    # Sort based on smallest to biggest.
    array = merge(firstHalf, secondHalf)
    return array

print(mergeSort([27,10,12,20,25,13,15,22]))
