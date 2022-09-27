#백준 10972번-다음 순열

#방법1- permutations 사용: 메모리초과
# import sys
# from itertools import permutations

# n = int(sys.stdin.readline())
# arr_list = []
# for i in range(1, n+1):
#     arr_list.append(i)

# all_list = list(permutations(arr_list, n))
# # for elem in all_list:
# #     print(elem)

# given_inputs = list(map(int, sys.stdin.readline().split()))
# x = tuple(given_inputs)

# y = all_list.index(x)

# if y != len(all_list)-1:
#     answer= all_list[y+1]
#     for elem in answer:
#         print(elem, end=' ')
# else:
#     print(-1)


#방법 2- next permutation 알고리즘 설계

import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, 0, -1):
    if num_list[i-1] < num_list[i]: #앞 숫자가 뒷 숫자보다 작을 경우
        for j in range(n-1, 0, -1):
            if num_list[i-1] < num_list[j]:
                num_list[i-1], num_list[j] = num_list[j], num_list[i-1] #두 값을 스왑
                a = (num_list[:i])
                b = sorted(num_list[i:])
                c = a + b
                print(*c)
                exit()
print(-1)