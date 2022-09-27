#백준 5554번-심부름 가는 길

import sys

ans = 0
for i in range(4):
	ans += int(sys.stdin.readline())
print(ans//60)
print(ans%60)