#백준 11004번-K번째 수

import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

print(nums[k-1])

