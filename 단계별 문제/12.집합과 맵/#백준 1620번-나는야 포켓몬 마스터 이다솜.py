#백준 1620번-나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    poketmon = sys.stdin.readline().strip()
    arr.append(poketmon)

given_list = []
for _ in range(m):
    x = sys.stdin.readline().strip()
    given_list.append(x)


for elem in given_list:
    if elem == elem.upper():    #숫자
        elem = int(elem)
        print(arr[elem-1])
    else:                       #문자열
        print(arr.index(elem)+1)

