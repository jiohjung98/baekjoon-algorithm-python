#백준 11050번-이항 계수1

# import sys

# n, k = map(int, sys.stdin.readline().split())

# x = 1
# for i in range(1,n+1):
#     x *= i

# y = 1
# for j in range(1, k+1):
#     y *= j

# z = 1
# for k in range(1, n-k+1):
#     z *= k
    
# print(x//(y*z))


#방법2- factorial 사용

import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, sys.stdin.readline().split())
print(factorial(n) // (factorial(k)* factorial(n-k)))