#백준 2164번-카드2

#방법 1- 시간초과(card 배열 생성 시간에서 초과)
# import sys

# n = int(sys.stdin.readline())
# card_list = []

# for i in range(1,n+1):
#     card_list.append(i)

# answer_list = []
# while True:
#     answer_list.append(card_list.pop(0))
#     if len(card_list) == 1:
#         print(card_list[0])
#         break
#     card_list.append(card_list.pop(0))


#방법 2- collections deque 사용해서 해결
import sys
import collections

n = int(sys.stdin.readline())
card = collections.deque([i for i in range(1,n+1)])

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()

print(card[0])



    