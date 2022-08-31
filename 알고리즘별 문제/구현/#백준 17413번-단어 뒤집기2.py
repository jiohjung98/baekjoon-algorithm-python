#백준 10988번-팰린도름인지 확인하기

import sys

given = list(map(str, sys.stdin.readline().strip()))
arr = []
left_arr = []
right_arr = []

if len(given) % 2 != 0: #홀수개
    middle = len(given) // 2 
    for i in range(middle-1, -1, -1):
        left_arr.append(given[i])
    for j in range(middle+1, len(given)):
        right_arr.append(given[j])
else:
    middle = len(given) // 2
    for i in range(middle-1, -1, -1):
        left_arr.append(given[i])
    for j in range(middle, len(given)):
        right_arr.append(given[j])

if left_arr == right_arr:
    print(1)
else:
    print(0)
        
    
