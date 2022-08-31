#백준 3009번-네 번째 점

# import sys

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# if x1 == x2:
#     if y1 == y2:
#         print(x3, y3)
#     elif y1 == y3:
#         print(x3, y2)
#     else: #y2 == y3
#         print(x3, y1)
# elif x1 == x3:
#     if y1 == y2:
#         print(x2, y3)
#     elif y1 == y3:
#         print(x2, y2)
#     else: #y2 == y3
#         print(x2, y1)
# else:
#     if y1 == y2:
#         print(x1, y3)
#     elif y1 == y3:
#         print(x1, y2)
#     else: #y2 == y3
#         print(x1, y1)


#방법 2- 더 간결한 코드-list 사용

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int ,input().split())
    x_list.append(x)
    y_list.append(y)
    
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x_list.append(x_list[i])
    if y_list.count(y_list[i]) == 1:
        y_list.append(y_list[i])

print(x_list[3], y_list[3])