#백준 10825번-국영수 

import sys

n = int(sys.stdin.readline())
students_list = []
for _ in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    students_list.append((name, int(kor), int(eng), int(math)))

sorted_list = sorted(students_list, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(sorted_list[i][0])
