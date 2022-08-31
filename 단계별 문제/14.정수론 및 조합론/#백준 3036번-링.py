#백준 3036번-링

import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

#최대공약수로 나눔

x = nums[0]
for i in range(1,n):
    for j in range(nums[i], 0, -1):
        if x % j == 0 and nums[i] % j == 0:
            y = x // j
            z = nums[i] // j
            print(f"{y}/{z}")
            break

            