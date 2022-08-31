#백준 2609번-최대공약수와 최소공배수

import sys

n, m = map(int, sys.stdin.readline().split())
z = min(n, m)

for i in range(z, 0, -1):
    if n % i == 0 and m % i == 0:
        x = i
        break


n_var = n // x
m_var = m // x

print(x)
print(x*n_var*m_var)


