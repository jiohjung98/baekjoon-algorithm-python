#백준 11866번-요세푸스 문제 0

#방법 1- 런타임 에러(index error)
# import sys

# n, k = map(int, sys.stdin.readline().split())

# people_list = [i for i in range(1, n+1)]
# answer_list = []

# for i in range(n):
#     if len(people_list) > 2:
#         if k > len(people_list):
#             answer_list.append(people_list[k-1])
#             for j in range(k):
#                 x = people_list[0]
#                 people_list.pop(0)
#                 people_list.append(x)
#             people_list.remove(people_list[-1])

# for elem in people_list:
#     answer_list.append(elem)

# print("<", end='')
# for i in range(len(answer_list)-1):
#     print("%d, "%answer_list[i], end='')
# print(answer_list[-1], end='')
# print(">")


#방법 2

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

people_list = [i for i in range(1, n+1)]
q_list = deque(people_list)
answer_list = []

while q_list:
    for i in range(k-1):
        q_list.append(q_list.popleft())
    answer_list.append(q_list.popleft())

print("<", end='')
for i in range(len(answer_list)-1):
    print(answer_list[i], end=', ')
print(answer_list[-1], end='')
print(">")