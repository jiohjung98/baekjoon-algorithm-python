#백준 2822번-점수 계산

import sys

score_list = []
for _ in range(8):
    score = int(sys.stdin.readline())
    score_list.append(score)

sorted_score_list = sorted(score_list)

n = 0
while True:
    if n == 3:
        break
    del sorted_score_list[0]
    n += 1

print(sum(sorted_score_list))
for elem in score_list:
    if elem in sorted_score_list:
        print(score_list.index(elem)+1, end=' ')