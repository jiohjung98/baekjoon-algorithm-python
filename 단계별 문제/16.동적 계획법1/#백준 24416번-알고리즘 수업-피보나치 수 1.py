#백준 24416번-알고리즘 수업-피보나치 수 1

import sys

#방법1- 피보나치 수 재귀함수
def fib(n):
    if (n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)



#방법2- DP(Tabulation-Bottom up(상향식))
def fib_Tab(n):
    dp_Tab = [0]*(n+1)
    dp_Tab[0] = 0
    dp_Tab[1] = 1
    dp_Tab[2] = 1
    cnt2 = 0

    for i in range(3, n+1):
        cnt2 += 1
        dp_Tab[i] = dp_Tab[i-1] + dp_Tab[i-2]

    return cnt2

n = int(sys.stdin.readline())
print(fib(n), fib_Tab(n))