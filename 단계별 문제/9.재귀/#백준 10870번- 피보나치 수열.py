#백준 10870번- 피보나치 수열

n = int(input())

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))