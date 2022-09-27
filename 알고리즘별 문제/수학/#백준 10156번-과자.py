#백준 10156번-과자

import sys

k, n, m = map(int, sys.stdin.readline().split())

answer= k*n-m
if answer > 0:
    print(answer)
else:
    print(0)