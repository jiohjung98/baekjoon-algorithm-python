#백준 1149번-RGB 거리

import sys

n = int(sys.stdin.readline())
cost_list = []

for _ in range(n):
    color_cost = list(map(int, sys.stdin.readline().split()))
    cost_list.append(color_cost)

def min_cost(n):
    dp = [0] * 50
    for i in range(3):


cost_list[0][0] 
1) [1][1] 
  1) [2][0]
  2) [2][2]

2) [1][2]
  1) [2][0]
  2) [2][1]

cost_list[0][1]

cost_list[0][2]