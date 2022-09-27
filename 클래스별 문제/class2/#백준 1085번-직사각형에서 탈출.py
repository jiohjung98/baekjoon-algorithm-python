#백준 1085번-직사각형에서 탈출

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(x,y,w,h,w-x,h-y))