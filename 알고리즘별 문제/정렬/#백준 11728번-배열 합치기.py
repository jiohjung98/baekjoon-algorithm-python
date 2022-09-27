#백준 11728번-배열 합치기

import sys

n, m = map(int, sys.stdin.readline().split())

a_array = list(map(int, sys.stdin.readline().split()))
b_array = list(map(int, sys.stdin.readline().split()))

c_array = sorted(a_array + b_array)

for elem in c_array:
    print(elem, end=' ')