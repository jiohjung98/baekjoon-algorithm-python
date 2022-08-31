#백준 1676번-팩토리얼 0의 개수

import sys

n = int(input())
cnt = 0

while n >= 5:
    cnt += n//5
    n //= 5

print(cnt)