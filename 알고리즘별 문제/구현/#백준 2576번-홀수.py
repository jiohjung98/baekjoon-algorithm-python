#백준 2576번-홀수

import sys
nums_arr = []

for _ in range(7):
    nums = int(sys.stdin.readline())
    nums_arr.append(nums)

odd_arr = []
for i in range(len(nums_arr)):
    if nums_arr[i] % 2 != 0:
        odd_arr.append(nums_arr[i])

if sum(odd_arr) != 0:
    print(sum(odd_arr))
    print(min(odd_arr))
else:
    print(-1)
