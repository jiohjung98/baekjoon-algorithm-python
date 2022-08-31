#백준 11478번-서로 다른 부분 문자열의 개수

import sys

s = sys.stdin.readline().strip()
answer = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        answer.add(s[i:j+1])

print(len(answer))