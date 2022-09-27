#백준 2960번-에레토스테네스의 체

import sys

# 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# 2 4 6 
# 2 4 6 8 10 12 14, 3 9 15, 5, 7

n, k = map(int, sys.stdin.readline().split())

cnt = 0

nums = [True] * (n+1)
x = int(n**0.5)
for i in range(2, x+1):
    if nums[i]:
        for j in range(i+i, n, i):
            nums[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break
