#백준 11444번-피보나치 수 6

import sys

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(sys.stdin.readline())
print(fibonacci(n))