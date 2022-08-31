#백준 9020번-골드바흐의 추측

from traceback import print_list


t = int(input())
for _ in range(t):
    n = int(input())
    
    arr = [True] * (n+1)
    arr[0] = 0
    arr[1] = 1
    
    m = int(n**0.5)
    
    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i, n, i):
                arr[j] = False
    
    prime_list = []
    for i in range(2, n):
        if arr[i] == True:
            prime_list.append(i)
    
    can_make_n = []
    for i in range(len(prime_list)):
        flag = False
        for j in range(i, len(prime_list)):
            if prime_list[i] + prime_list[j] == n:
                can_make_n.append(prime_list[i])
                can_make_n.append(prime_list[j])
                flag = True
            break
        if(flag): break
          
    print(can_make_n)
    
#     list_leng = len(prime_list)
#     if list_leng % 2 == 0:
#         left_list = prime_list[:list_leng//2]
#         right_list = prime_list[list_leng//2:]
#     else:
#         left_list = prime_list[:list_leng//2 + 1]
#         right_list = prime_list[list_leng//2 + 1:]
    
#     left_leng = len(left_list)
#     right_leng = len(right_list)
    
#     print(prime_list)
#     print(left_list)
#     print(right_list)
    
#     arr2 = [] 
#     for i in range(left_leng-1,0,-1):
#         for j in range(right_leng-1):
#             if left_list[i] + right_list[j] == n:
#                 arr2.append(left_list[i])
#                 arr2.append(right_list[j])
#     break
    
# print(arr2[0], arr2[1])

    
    