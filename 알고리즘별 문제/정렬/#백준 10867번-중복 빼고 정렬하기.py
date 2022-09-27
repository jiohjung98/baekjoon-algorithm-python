#백준 10867번-중복 빼고 정렬하기

import sys

n = int(sys.stdin.readline())
nums_list = list(map(int, sys.stdin.readline().split()))

nums_list = list(set(nums_list))
nums_list.sort()

for elem in nums_list:
    print(elem, end=' ')