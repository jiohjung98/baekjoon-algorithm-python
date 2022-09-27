#백준 2960번-에라토스테네스의 체

import sys

n, k = map(int, sys.stdin.readline().split())


num_list = [True] * (n+1)
x = int(n**0.5)
cnt = 0

for i in range(2, n+1):
    if num_list[i] == True:
        for j in range(i, n+1, i):
            if num_list[j] == True:
                num_list[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    break