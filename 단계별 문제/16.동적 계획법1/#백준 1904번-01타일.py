#백준 1904번-01타일

import sys

def zero_one_tile(n):
    dp = [0] * (1000001)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    return dp[n]

n = int(sys.stdin.readline())
print(zero_one_tile(n))