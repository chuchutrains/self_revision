# https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/

# Option 1.
# Make use of try-except.
def duplicate(arr):
    dic = {}
    for x in arr:
        # Increment value to indicate it is duplicate.
        try:
            dic[x] += 1
        # Create new key.
        except:
            dic[x] = 1

    duplicates = []
    for x in dic:
        if dic[x] > 1:
            duplicates.append(x)
    return duplicates

# Option 2.
# Make use of set().
def duplicate2(arr):
    unqiue = set()
    duplicates = []
    for x in arr:
        if x in unqiue:
            duplicates.append(x)
        else:
            unqiue.add(x)
    return duplicates

arr = [5,4,3,2,1,3]
print(duplicate(arr))
# print(duplicate2(arr))