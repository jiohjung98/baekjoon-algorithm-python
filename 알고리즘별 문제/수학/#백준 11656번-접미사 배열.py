#백준 11656번-접미사 배열

import sys

s = sys.stdin.readline().strip()

new_list = []
# while True:
#     if len(s) == 0:
#         break
#     s.remove(s[0])
#     new_list.append(s)

for _ in s:
    new_list.append(s)
    s = s[1:]

new_list = sorted(new_list)

for elem in new_list:
    print(elem, end='\n')