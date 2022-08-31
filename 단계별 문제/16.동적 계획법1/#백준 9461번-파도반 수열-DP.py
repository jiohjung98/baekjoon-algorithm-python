#백준 9461번-파도반 수열-DP

import sys

def padovan_seq(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1], dp[2], dp[3] = 1, 1, 1

    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    return dp[n]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    if n == 1 or n == 2:
        print(1)
    else:
        print(padovan_seq(n))