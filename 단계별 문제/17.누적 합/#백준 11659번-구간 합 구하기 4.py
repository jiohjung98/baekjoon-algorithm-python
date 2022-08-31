#백준 11659번-구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

#누적 합 구하기 
new_arr = []
sum_val = 0
for elem in nums:
    sum_val += elem
    new_arr.append(sum_val)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        print(new_arr[y-1])
    else:
        print(new_arr[y-1] - new_arr[x-2])
