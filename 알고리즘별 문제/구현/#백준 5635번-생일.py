#백준 5635번-생일

import sys

n = int(sys.stdin.readline())
students_list = []


for _ in range(n):
    name, day, month, year = map(str, sys.stdin.readline().split())
    day, month, year = int(day), int(month), int(year)
    students_list.append([name, day, month, year])

arrayed_list = sorted(students_list, key = lambda x: (x[3], x[2], x[1]))

print(arrayed_list[-1][0])
print(arrayed_list[0][0])
