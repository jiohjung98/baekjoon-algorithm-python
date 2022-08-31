# 백준 2004번-조합 0의 개수

# 방법1- 런타임에러
# import sys

# n , m = map(int, sys.stdin.readline().split())

# # 25 24 23 22 21 20 19 18 17 16 15 14 
# x = 1
# for i in range(n, (n-m), -1):
#     x *= i

# y = 1
# for i in range(m, 1, -1):
#     y *= i

# z = list(str(x//y))

# cnt = 0
# for i in range(len(z)-1, 0, -1):
#     if z[i] == '0':
#         cnt += 1
#     else:
#         break

# print(cnt)


#방법2- 2,5의 개수를 세는 방법
import sys

def five_count(n):
    answer = 0
    while n != 0:
        n //= 5
        answer += n
    return answer

def two_count(n):
    answer = 0
    while n != 0:
        n //= 2
        answer += n
    return answer
        
n, m = map(int, sys.stdin.readline().split())

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))