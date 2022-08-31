#백준 9375번-패션왕 신해빈

# import sys
# import itertools

# n = int(sys.stdin.readline())
# cnt_list = []
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     clothes_list = []
#     cnt = 0
#     for _ in range(x):
#         clothes = sys.stdin.readline().strip()
#         if ' ' in clothes:
#             y = clothes.index(' ')
#         clothes_list.append(clothes[y+1:])
#     for i in range(1, len(clothes_list)+1):
#         result = list(itertools.combinations(clothes_list, i))
#         cnt += len(result)
#     for i in range(len(clothes_list)-1):
#         for j in range(i+1, len(clothes_list)):
#             if clothes_list[i] == clothes_list[j]:
#                  cnt -= 1
#     cnt_list.append(cnt)
#     if len(set(clothes_list)) != 1:
    #     cnt += 1
    # print(cnt)
    

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    clothes_list = [] #옷의 종류
    clothes_count = [] #종류별 옷의 개수
    
    for i in range(int(sys.stdin.readline())):
        x, y = sys.stdin.readline().split()
        
        if y in clothes_list:
            clothes_count[clothes_list.index(y)] += 1
        else:
            clothes_list.append(y)
            clothes_count.append(2) #입지 않는 경우도 있으므로 2를 추가(입는거 1, 안입는거 1)
            
    result = 1
    for i in clothes_count:
        result *= i
    print(result-1)