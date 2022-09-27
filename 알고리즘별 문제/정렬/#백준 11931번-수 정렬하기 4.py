#백준 11931번-수 정렬하기 4

import sys

n = int(sys.stdin.readline())

num_list = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
]

num_list.sort(reverse=True)

for elem in num_list:
    print(elem, end='\n')