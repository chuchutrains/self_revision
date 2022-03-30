# Complexity O(x).
def mul(x,y):
    n = x
    sum = 0
    while n > 0:
        sum = sum + y
        n = n - 1
    return sum

print(mul(2,3))