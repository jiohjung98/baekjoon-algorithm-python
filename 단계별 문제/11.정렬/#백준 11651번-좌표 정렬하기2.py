#백준 11651번-좌표 정렬하기2

# 방법1- 시간초과
# import sys

# n = int(sys.stdin.readline())
# arr = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     temp = a
#     a = b
#     b = temp
#     arr.append((a,b))
    
# arr.sort()
# for i in range(n):
#     print(arr[i][1], arr[i][0])


#방법2
import sys

n = int(sys.stdin.readline())
arr = [] 
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a, b = b, a
    arr.append((a,b))

arr.sort()  

for i in range(n):
    print(arr[i][1], arr[i][0])
