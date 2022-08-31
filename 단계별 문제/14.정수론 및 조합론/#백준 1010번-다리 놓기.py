#백준 1010번-다리 놓기

import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))

