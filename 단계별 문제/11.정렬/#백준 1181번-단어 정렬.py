#백준 1181번-단어 정렬

import sys

n = int(sys.stdin.readline())
new_list = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    if word not in new_list:
        new_list.append(word)

new_list.sort()
new_list.sort(key = len)
       
for elem in new_list:
    print(elem)

