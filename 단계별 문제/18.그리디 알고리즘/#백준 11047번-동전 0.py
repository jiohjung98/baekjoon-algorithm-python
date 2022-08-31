#백준 11047번-동전 0

import sys

n, k = map(int, sys.stdin.readline().split())

coin_list = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)
    
cnt = 0
coin_list.sort(reverse=True)

for i in range(len(coin_list)):
    if k >= coin_list[i]:
        div = k % coin_list[i]
        cnt += k // coin_list[i]
        k = div
print(cnt)