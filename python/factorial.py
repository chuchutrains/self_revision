def factorial(n):
    if n==0:
        answer = 1
    else:
        answer = n * factorial(n-1)
    return answer

print(factorial(5))