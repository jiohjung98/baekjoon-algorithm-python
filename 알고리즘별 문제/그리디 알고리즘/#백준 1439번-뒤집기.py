#백준 1439번-뒤집기

import sys

s = sys.stdin.readline()
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print(cnt//2)