#백준 4948번-베르트랑 공준(소수)

#방법 1- 답은 맞으나 시간초과 뜸
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     double_n = 2*n
#     cnt = double_n - n 
#     for i in range(n+1, double_n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 cnt -= 1
#                 break
#     print(cnt)

#- 에라토스테네스의 체 
# def prime_list(n):
#     arr = [True] * n 
    
#     m = int(n**0.5) #제곱근씌우기 ex) n=16 -> m=4
#     for i in range(2, m+1):
#         if arr[i] == True:
#             for j in range(i+i,n,i): #i+i부터 n까지 i씩 증가하면서 i의 배수들 탐색
#                 arr[j] = False
    
#     # prime_arr= []
#     # for i in range(2,n):
#     #     if arr[i] == True:
#     #         prime_arr.append(i)
    
#     # return prime_arr
    
#     #위의 5문장을 한 문장으로 코드 작성 가능
#     return [i for i in range(2,n) if arr[i] == True]

# 1. n*2까지의 소수를 구한다(3,5,7,11,13,17,19)
# 2. if arr[i] > n:
#     새 배열에 어펜드

# while True:
#     n = int(input())
#     if n == 0:
#         break
    
#     double_n = 2*n
#     arr = [True] * double_n
    
#     m = int(double_n**0.5) 
#     for i in range(2, m+1):
#         if arr[i] == True:
#             for j in range(i+i, double_n, i):
#                 arr[j] = False
    
#     all_prime_num= [] 
#     cnt = 0
#     for i in range(2, double_n):
#         if arr[i] == True:
#             all_prime_num.append(i)
#             cnt += 1
    
#     for i in range(len(all_prime_num)):
#         if all_prime_num[i] <= n:
#             cnt -= 1
    
#     print(cnt)
     
    
                
while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        double_n = n*2

        arr = [True] * double_n

        m = int(double_n**0.5)

        for i in range(2, m+1):
            if arr[i] == True:
                for j in range(i+i, double_n, i):
                    arr[j] = False

        all_prime_num = []
        in_range_cnt = 0
        for i in range(2, double_n):
            if arr[i] == True:
                all_prime_num.append(i)
                in_range_cnt += 1

        for elem in all_prime_num:
            if elem <= n:
                in_range_cnt -= 1

        print(in_range_cnt)
        
            
    
    
    
    
    
    
    
    
    