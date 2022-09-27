#백준 10973번-이전 순열

import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, 0, -1):
    if num_list[i-1] > num_list[i]:
        for j in range(n-1, 0, -1):
            if num_list[i-1] > num_list[j]:
                num_list[i-1], num_list[j] = num_list[j], num_list[i-1]
                a = num_list[:i]
                b = num_list[i:]
                b.sort(reverse=True)
                c = a + b
                print(*c)
                exit()
print(-1)
#     for j in range(i-1, 0, -1):
#         if num_list[i] < num_list[j]:
#             num_list[i], num_list[j] = num_list[j], num_list[i]
#             if j == i-1: #맨 끝 index
#                 print(*num_list)
#                 exit()
#             else:
#                 a = num_list[:i-1]
#                 b = num_list[i-1:]
#                 b.sort(reverse=True)
#                 c = a+b
#                 print(*c)
#                 exit()
# print(-1)














#     for j in range(i-1, 0, -1):
#         if num_list[i] < num_list[j]:
#             num_list[i], num_list[j] = num_list[j], num_list[i]
#             a = num_list[:i]
#             b = num_list[i:]
#             c = a + b
#             if num_list[j] < num_list[i]:
#                 d = c[i-1:]
#                 d.sort(reverse=True)
#             e = c[:i-1]
#             f = e + d
#             print(*f)
#             exit()
# print(-1)
#         for j in range(n-1, 0, -1):
#             if num_list[i] < num_list[j]:
#                 num_list[i-1], num_list[j] = num_list[j], num_list[i-1]
#                 a = num_list[:i]
#                 b = num_list[i:]
#                 b.sort(reverse=True)
#                 c = a + b
#                 print(*c)
#                 exit()
#             else:
#                 num_list[i-1], num_list[i] = num_list[i], num_list[i-1]
#                 print(*num_list)
#                 exit()

# print(-1)