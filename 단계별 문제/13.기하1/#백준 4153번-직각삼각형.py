# #백준 4153번-직각삼각형

# x_list= []
# y_list= []
# z_list= []

# while True:
#     x, y, z = map(int, input().split())
#     if x == 0 and y == 0 and z == 0:
#         break
#     x_list.append(x)
#     y_list.append(y)
#     z_list.append(z)

# for i in range(len(x_list)):
#     max_val = max(x_list[i], y_list[i], z_list[i])
#     remainder = []
#     remainder.append(x_list[i])
#     remainder.append(y_list[i])
#     remainder.append(z_list[i])
#     remainder.remove(max_val)
#     if max_val**2 == remainder[0]**2 + remainder[1]**2:
#         print("right")
#     else:
#         print("wrong")
            

#방법2- 더 간결함

while True:
    list_ = list(map(int, input().split()))
    max_num = max(list_)
    if sum(list_) == 0:
        break
    list_.remove(max_num)
    if max_num**2 == list_[0]**2 + list_[1]**2:
        print("right")
    else:
        print("wrong")