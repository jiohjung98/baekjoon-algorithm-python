#백준 11051번-이항 계수2

#방법 1- factorial 함수 이용
import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split())


x = factorial(n) // (factorial(k)*factorial(n-k))
print(x%10007)