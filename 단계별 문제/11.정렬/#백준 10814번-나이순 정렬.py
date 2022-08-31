#백준 10814번-나이순 정렬

import sys

n = int(sys.stdin.readline())
user= []
for _ in range(n):
    user.append(list(sys.stdin.readline().split()))

#나이를 기준으로 정렬

user.sort(key=lambda x: int(x[0]))

for elem in user:
    print(elem[0], elem[1])