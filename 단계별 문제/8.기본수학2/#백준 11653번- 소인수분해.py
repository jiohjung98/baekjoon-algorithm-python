#백준 11653번- 소인수분해

n = int(input())

for i in range(2, n+1):
    while n % i == 0:
        n = n // i
        print(i)
    if n == 1:
        break
