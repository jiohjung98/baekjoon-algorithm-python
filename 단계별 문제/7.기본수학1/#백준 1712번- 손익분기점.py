#백준 1712번- 손익분기점

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    n = a // (c-b)
    n += 1
    print(n)

    