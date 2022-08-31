#백준 1912번-연속합

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sum = [arr[0]]

for i in range(len(arr)-1):
    sum.append(max(sum[i]+arr[i+1], arr[i+1]))

print(max(sum))
