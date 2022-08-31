#백준 2161번-카드1

import sys

n = int(sys.stdin.readline())
card = [
    i for i in range(1,n+1)
]

# card = []
# for i in range(1, n+1):
#     card.append(i)
    
answer = []

while True:
    answer.append(card.pop(0))
    if len(card) == 0:
        break
    card.append(card.pop(0))

print(*answer)
