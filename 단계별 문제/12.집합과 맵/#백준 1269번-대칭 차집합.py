#백준 1269번-대칭 차집합

#방법1- 리스트 사용
# import sys

# a, b = map(int, sys.stdin.readline().split())

# arr1 = list(map(int, sys.stdin.readline().split()))
# arr2 = list(map(int, sys.stdin.readline().split()))

# overlap = list(set(arr1) & set(arr2))
# cnt = (len(arr1)-len(overlap)) + (len(arr2)-len(overlap))
# print(cnt)


#방법2- set 사용
import sys

a, b = map(int, sys.stdin.readline().split())
arr1 = set(map(int, sys.stdin.readline().split()))
arr2 = set(map(int, sys.stdin.readline().split()))

print(len(arr1-arr2)+len(arr2-arr1))
