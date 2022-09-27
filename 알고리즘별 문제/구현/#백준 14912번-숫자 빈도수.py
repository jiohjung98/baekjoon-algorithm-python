#백준 14912번-숫자 빈도수

import sys

n, k = map(int, sys.stdin.readline().split())
ans = 0
for i in range(1, n+1):
    ans += str(i).count(str(k))

print(ans)