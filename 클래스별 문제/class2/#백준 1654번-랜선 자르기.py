#백준 1654번-랜선 자르기

import sys

k, n = map(int, sys.stdin.readline().split())
length_list = []

for _ in range(k):
    length = int(sys.stdin.readline())
    length_list.append(length)

