#백준 11650번-좌표 정렬하기

import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])