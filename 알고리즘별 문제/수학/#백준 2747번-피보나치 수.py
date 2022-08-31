#백준 2747번-피보나치 수

#방법1- 시간초과
# import sys

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(sys.stdin.readline())
# print(fibonacci(n))


#방법2- for문 이용

import sys

n = int(sys.stdin.readline())
x, y = 0 , 1

while n > 0:
    x, y = y, x+y
    n -= 1

print(x)
