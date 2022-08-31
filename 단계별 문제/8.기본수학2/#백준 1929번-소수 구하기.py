#백준 1929번-소수 구하기

#방법1 - 시간 초과뜸
# m, n = map(int, input().split())

# arr1 = [
#     i
#     for i in range(m, n+1)
# ]

# arr2 = []
# for i in range(m, n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             arr2.append(i)
#             break

# arr3= [] 
# for elem in arr1:
#     if elem not in arr2:
#         arr3.append(elem)

# if 1 in arr3:
#     arr3.remove(1)
        
# for i in range(len(arr3)):
#     print(arr3[i], end='\n')


#방법2
m, n = map(int, input().split())

arr = [True] * (n+1)
arr[0] = 0
arr[1] = 1
x = int(n**0.5)

for i in range(2, x+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

prime_list = []
for i in range(2, len(arr)):
    if arr[i] == True:
        prime_list.append(i)

# for elem in prime_list:
#     if elem < m:
#         prime_list.remove(elem)   
#코드 질문 

#답
# 18번째 코드를 실행하기 전에 prime_list = [2, 3, 5, 7, 11, 13, 17, 19]입니다.

# 여기서 첫번째부터 마지막까지 순서대로 확인할텐데, 먼저 첫 번째인 2가 10보다 작으니 2를 뺍니다.

# 그러면 [3, 5, 7, 11, 13, 17, 19] 가 되겠죠?

# 그럼 첫 번째껀 확인했으니 for문은 여기서 두 번째 걸 가져옵니다.

# 그러면 5를 가져오게 되는 거죠. 그러면 5가 빠지고 3은 건너뛰게 됩니다.

# 7도 마찬가지로 건너뛰게 됩니다.

in_range_prime_num = []
for i in range(len(prime_list)):
    if prime_list[i] >= m:
        in_range_prime_num.append(prime_list[i])

for elem in in_range_prime_num:
    print(elem, end='\n')

# for elem in prime_list:
#     print(elem, end='\n')


        