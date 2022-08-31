#백준 1931번-회의실 배정

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    times = list(map(int, sys.stdin.readline().split()))
    arr.append(times)
    
arr.sort(key=lambda x: x[0]) 
arr.sort(key=lambda x: x[1])

cnt = 1
end = arr[0][1]

for i in range(1, n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]

print(cnt)

