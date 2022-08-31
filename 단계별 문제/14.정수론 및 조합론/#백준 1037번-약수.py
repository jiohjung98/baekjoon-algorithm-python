#백준 1037번-약수

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

answer = max(nums) * min(nums)
print(answer)