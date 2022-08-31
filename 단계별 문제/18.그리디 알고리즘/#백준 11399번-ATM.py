#백준 11399번-ATM

import sys

n = int(sys.stdin.readline())
people_times = list(map(int, sys.stdin.readline().split()))

people_times.sort()

sum_val = 0
for i in range(n):
    sum_val += sum(people_times[0:i+1])

print(sum_val)