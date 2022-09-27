#백준 5800번-성적 통계

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    class_list = list(map(int, sys.stdin.readline().split()))
    class_list.remove(class_list[0])
    class_list.sort()
    print(f"Class {i}")
    class_list.sort(reverse=True)
    diff = class_list[0] - class_list[1]
    for i in range(1, len(class_list)-1):
        if (class_list[i] - class_list[i+1]) > diff:
            diff = class_list[i] - class_list[i+1]
    print(f"Max {max(class_list)}, Min {min(class_list)}, Largest gap {diff}")

