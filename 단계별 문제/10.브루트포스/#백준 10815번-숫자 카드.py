#백준 10815번-숫자 카드

#방법1- 시간초과
# n = int(input())
# cards = list(map(int, input().split()))

# m = int(input())
# given_cards = list(map(int, input().split()))

# for card in given_cards:
#     if card in cards:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


#방법2- 이분 탐색 사용
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
given_cards = list(map(int, input().split()))
cards.sort()

def binary_search(a, x):
    start = 0
    end = len(a)-1
    
    while start <= end:
        mid = (start+end)//2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for elem in given_cards:
    print(binary_search(cards, elem), end=' ')