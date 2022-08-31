#백준 2675번- 문자열 반복

t = int(input())

for _ in range(t):
    r, given = input().split()
    r = int(r)
    for elem in given:
        print(elem*r, end='')
    print("\n")