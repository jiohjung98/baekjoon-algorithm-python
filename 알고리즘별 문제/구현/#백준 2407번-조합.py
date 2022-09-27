#백준 2407번-조합 
#조합- 서로 다른 n개 중 m개를 선택하는 경우의 수(순서없음)
#nCm = n! / (n-m)! * m!

import sys
import math

n, m = map(int, sys.stdin.readline().split())
print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))


