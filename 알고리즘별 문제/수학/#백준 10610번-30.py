#백준 10610번-30

#방법1- 메모리초과 
# import sys
# from itertools import permutations

# n = list(map(str, sys.stdin.readline().strip()))

# x = list(permutations(n, len(n)))

# result = []
# for i in range(len(x)):
#     y = "".join(x[i])
#     result.append(y)
    
# int_result = list(map(int, result))
# int_result.sort(reverse=True)
# answer= []
# for i in range(len(int_result)):
#     if int_result[i] % 30 == 0:
#         print(int_result[i])
#         break
#     else:
#         print(-1)
#         break
    
    
#방법2
#1. 30의 배수이므로 주어진 숫자에 0이 포함되어있지 않으면 틀림(10의 배수)
#2. 30의 배수이므로 각 숫자를 다 더했을 때 3의 배수여야 함! 


n = input()
n = sorted(n, reverse=True)

m = 0
if '0' not in n:
    print('-1')
else:
    for i in n:
        m += int(i)
    if m % 3 != 0:
        print('-1')
    else:
        print(''.join(n))


    