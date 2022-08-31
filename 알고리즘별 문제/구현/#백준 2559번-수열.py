#백준 2559번-수열

#방법1- 시간초과
# import sys

# n, k = map(int, sys.stdin.readline().split())
# temper_arr = list(map(int, sys.stdin.readline().split()))

# sum_list = []

# for i in range(n-k+1):
#     sum_list.append(sum(temper_arr[i:i+k]))
    
# print(max(sum_list))


#방법 2
import sys

n, k = map(int, sys.stdin.readline().split())
temper_arr = list(map(int, sys.stdin.readline().split()))

sum_list = [sum(temper_arr[:k])]

print(sum_list)