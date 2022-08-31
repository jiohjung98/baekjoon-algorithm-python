#백준 1463번-1로 만들기

import sys

def fibo(n):
    cnt = 0
    
    if n == 1:
        return cnt
    elif n % 3 != 0:
        if (n-1) % 3 == 0:
            n = n-1
            cnt += 1
            return fibo(n)
        elif (n-2) % 3 == 0:
            n = n-2
            cnt += 1
            return fibo(n)
    elif n % 3 == 0:
        n = n//3
        cnt += 1
        return fibo(n)
    elif n % 2 == 0:
        n == n//2
        cnt += 1
        return fibo(n)
    
n = int(input())
print(fibo(n))
    