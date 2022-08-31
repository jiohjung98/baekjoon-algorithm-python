#백준 10816번-숫자 카드2

#방법1- 시간초과
# import sys

# n = int(sys.stdin.readline())
# card_list = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# find_card = list(map(int, sys.stdin.readline().split()))

# for i in range(m):
#     i = find_card[i]
#     print(card_list.count(i), end=' ')


#방법 2- 이진 탐색 사용

import sys

def binary_search(list, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if list[mid] == target:
        return cnt.get(target)
    elif list[mid] > target:
        return binary_search(list, target, start, mid-1)
    else:
        return binary_search(list, target, mid+1, end)

n = int(sys.stdin.readline())
card_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
find_card = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in card_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in find_card:
    print(binary_search(card_list, i, 0, len(card_list)-1), end=' ')