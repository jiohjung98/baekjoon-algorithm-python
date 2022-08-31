#백준 2108번-통계학

import sys
from collections import Counter

n = int(sys.stdin.readline())
arr= []

for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    
sum_avg = sum(arr) / n  #산술평균
arr.sort()              #중앙값 내주기
x = max(arr)            #최대값
y = min(arr)            #최소값

cnt = Counter(arr).most_common(2)

print(round((sum_avg)))
print(arr[n//2])
if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(x-y)
    
