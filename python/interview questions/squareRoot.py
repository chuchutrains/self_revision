# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are tuncated, and
# only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or
# operator,  such as pow(x, 0.5) or x ** 0.5.

def sqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (right+left) // 2
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            left = mid + 1
        else:
            right = mid - 1
        print(left,mid,right)
    return right

print(sqrt(37))