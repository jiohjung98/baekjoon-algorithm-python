#백준 6603번-로또

import sys
from itertools import combinations

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if sum(nums) == 0:
        break
    nums_cnt = nums[0]
    nums.remove(nums_cnt)
    arr = []
    for i in combinations(nums, 6):
        arr.append(i)
    for i in range(len(arr)):
        for j in range(6):
            print(arr[i][j], end=' ')
        print()
    print()