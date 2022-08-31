#백준 10809번-알파벳 찾기

alphabet = "abcdefghijklmnopqrstuvwxyz"

n = input()
n = list(n)

for elem in alphabet:
    if elem in n:
        print(n.index(elem), end=' ')
    else:
        print(-1, end=' ')

    