
x = int(input())
n = int(input())
total_price = 0

for _ in range(n):
    price, cnt = map(int, input().split())
    total_price += price * cnt

if x == total_price:
    print('Yes')
else:
    print('No')