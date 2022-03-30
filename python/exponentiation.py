# Complexity O(n).
def power(a,n):
    answer = 1
    for i in range(n):
        answer = answer * a
    return answer

#print(power(2,3))

# FAST exponentiation. Divide and conquer complexity O(log N).
def power2(a,n):
    if n==0: 
        print(1)
        return 1
    answer = power2(a, (int)(n/2))
    
    if n%2 == 0:
        print('e', answer)
        return answer * answer
    else:
        print('o', answer)
        return answer  * answer * a

print(power2(2,4))