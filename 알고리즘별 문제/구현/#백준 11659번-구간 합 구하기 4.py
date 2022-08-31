#백준 11659번-구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

temp = []
sum_val = 0
for elem in arr:
    sum_val += elem
    temp.append(sum_val)
    
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        print(temp[y-1])
    else:
        print(temp[y-1]-temp[x-2])