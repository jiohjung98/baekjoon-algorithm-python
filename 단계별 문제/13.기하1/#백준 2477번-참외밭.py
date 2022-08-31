#백준 2477번-참외밭

n = int(input())
len_list = []
for _ in range(6):
    len_ = list(map(int, input().split()))
    len_list.append(len_)


width_list = []
length_list = []
for i in range(6):
    if len_list[i][0] == 1 or len_list[i][0] == 2:
        width_list.append(len_list[i][1])
        max_width = max(width_list)
    if len_list[i][0] == 3 or len_list[i][0] == 4:
        length_list.append(len_list[i][1])
        max_length = max(length_list)
        
for i in range(4): #i=0,1,2,3
    if len_list[i][0] == len_list[i+2][0]: 
        if i != 0:
            x = len_list[i+1][1]
            y = len_list[i+2][1]
            break
        else: #i = 0
            if len_list[i+1][0] == len_list[i+3][0]:
                x = len_list[i+1][1]
                y = len_list[i+2][1]
                break
            else:
                x = len_list[0][1]
                y = len_list[1][1]
                break
    else:
        x = len_list[0][1]
        y = len_list[-1][1]

remove_area = x*y
real_area = (max_length*max_width) - (remove_area)
print(real_area*n)