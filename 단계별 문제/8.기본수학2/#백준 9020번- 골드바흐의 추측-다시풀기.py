#백준 9020번- 골드바흐의 추측
from sys import stdin
arr = [True] * 10001
arr[0] = 0
arr[1] = 1

for i in range(2, 10001):
    if arr[i] == True:
        if arr[i] == False:
            continue
    for j in range(i+i, 10001, i):
        arr[j] = False

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    a = int(n/2)
    b = int(n/2)
    
    for i in range(int(n/2)):
        if arr[a] == True and arr[b] == True:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
        























# def self_num(n):
#     for i in range(len(self_list)):
#         if (self_list[i] > n/2):
#             break
#         for j in range(i, len(self_list)):
#             if (self_list[j] > n):
#                 break
#             if self_list[i] + self_list[j] == n:
#                 result1 = self_list[i]
#                 result2 = self_list[j]
#     return result1, result2