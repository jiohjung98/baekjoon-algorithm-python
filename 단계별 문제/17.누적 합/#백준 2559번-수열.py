#백준 2559번-수열

#방법1- 시간초과
# import sys

# n, k = map(int, sys.stdin.readline().split())
# temper_arr = list(map(int, sys.stdin.readline().split()))

# sum_list = []

# for i in range(n-k+1):
#     sum_list.append(sum(temper_arr[i:i+k]))
    
# print(max(sum_list))

import sys

n, k = map(int, sys.stdin.readline().split())
temper_list = list(map(int, sys.stdin.readline().split()))

temper_sum = []
temper_sum.append(sum(temper_list[:k]))

for i in range(n-k):
    temper_sum.append(temper_sum[i]-temper_list[i]+temper_list[i+k])

print(max(temper_sum))