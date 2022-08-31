#백준 2981번-검문

#방법 1- 시간초과
# import sys

# n = int(sys.stdin.readline())

# arr = []
# for _ in range(n):
#     num = int(sys.stdin.readline().strip())
#     arr.append(num)

# answer= []

# for j in range(2, min(arr)+1):
#     arr2 = []
#     for i in range(n):
#         arr2.append(arr[i] % j)
#     x = max(arr2)
#     if n == arr2.count(x):
#         answer.append(j)

# for elem in answer:
#     print(elem, end=' ')


#방법2
from math import gcd
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort(reverse=True)

nums_gap = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        nums_gap.append(arr[i]-arr[j])

nums_gap.sort()
min_nums_gap = nums_gap[0]
for i in range(1, len(nums_gap)):
    min_nums_gap = gcd(min_nums_gap, nums_gap[i])

answer= []
for i in range(2, int(min_nums_gap ** 0.5)+1):
    if min_nums_gap % i == 0:
        answer.append(i)
        answer.append(min_nums_gap//i)
answer.append(min_nums_gap)
answer = list(set(answer))
answer.sort()
print(*answer)





# answer= []
# for i in range(2, min(nums_gap)):
#     arr2=[]
#     for j in range(len(nums_gap)):
#         x = nums_gap[j] % i
#         arr2.append(x)
#     if arr2.count(x) == len(nums_gap):
#         answer.append(i)

# answer.append(nums_gap[0])

# for elem in answer:
#     print(elem, end=' ')
    
    
    
    
    
    
    
