#백준 1920번-수 찾기

import sys

n = int(sys.stdin.readline())
given_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
given_list2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for elem in given_list:
    dic[elem] = 1

for elem in given_list2:
    if elem in dic:
        print(1)
    else:
        print(0)