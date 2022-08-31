#백준 15650번-N과 M(2)

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

def back(start_num):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start_num, n+1):
        if i not in arr:
            arr.append(i)
            back(i+1)
            arr.pop()
back(1)