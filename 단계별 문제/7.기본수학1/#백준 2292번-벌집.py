#백준 2292번-벌집

n = int(input())

beehouse = 1
cnt = 1

while n > beehouse:
    beehouse += beehouse*cnt
    cnt += 1

print(cnt)
    