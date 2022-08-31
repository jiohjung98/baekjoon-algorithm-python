#백준 2839번-설탕 배달

n = int(input())
cnt = 0

if n >= 5:
    if n % 5 == int(0):
        cnt += n // 5
    elif n % 5 == int(1):
        n -= 6 
        cnt += 2
        cnt += n // 5
    elif n % 5 == int(2):
        if n >= 17:
            n -= 12
            cnt += n // 5
            cnt += 4
        else:
            if n % 3 == int(0):
                cnt += 4
            else:
                cnt -= 1
    elif n % 5 == int(3):
        cnt += n // 5
        cnt += 1
    elif n % 5 == int(4):
        if n >= int(14):
            n -= 9
            cnt += 3
            cnt += n // 5
        else:
            cnt += 3
else:
    if n == int(3):
        cnt += 1
    else:
        cnt -= 1

print(cnt)