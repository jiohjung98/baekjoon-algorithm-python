#백준 1934번-최소공배수

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    c = min(a,b)
    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            x = i
            break
    print((a*b)//x)