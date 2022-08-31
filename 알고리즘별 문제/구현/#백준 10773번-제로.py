#백준 10773번-제로

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline())
    #입력값이 0이면 pop, 아니면 push
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))