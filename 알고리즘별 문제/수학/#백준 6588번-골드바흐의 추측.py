#백준 6588번-골드바흐의 추측
#에라토스테네스의 체 사용(소수 판별)

import sys

x = 1000001
prime_list = [True for _ in range(x)]
y = int(x**0.5)
for i in range(2, y+1):
    if prime_list[i] == True:
        for j in range(i+i, x, i):
            prime_list[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    for i in range(3, len(prime_list)):
        if prime_list[i] == True and prime_list[n-i] == True:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
        break



