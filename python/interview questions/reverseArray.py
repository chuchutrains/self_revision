# Option 1
def reverse1(arr):
    revArr = []
    for i in range(len(arr)-1, 0-1, -1):
        revArr.append(arr[i])
    return revArr

# Option 2
def reverse2(arr):
    arrLen = len(arr)
    mid = arrLen // 2
    for i in range(mid):
        arr[i], arr[arrLen-1-i] = arr[arrLen-1-i], arr[i]
    return arr

arr = [1,2,3,4,5]
print(reverse1(arr))
print(reverse2(arr))
