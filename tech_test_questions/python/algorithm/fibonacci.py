def f(n):
    if n==0: return 0
    if n==1: return 1
    if n>=2: return f(n-1) + f(n-2)

#0,1,1,2,3,5,8,13,21,34..
print(f(6))