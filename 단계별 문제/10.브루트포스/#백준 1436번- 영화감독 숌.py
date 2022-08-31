#백준 1436번- 영화감독 숌

import sys
INT_MAX = sys.maxsize

arr= []
for i in range(INT_MAX):
    i = str(i)
    if '666' in i:
        arr.append(i)
n = int(input())
print(arr[n-1])