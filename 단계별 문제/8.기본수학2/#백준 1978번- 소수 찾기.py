#백준 1978번- 소수 찾기

n = int(input())

nums = list(map(int, input().split()))
cnt = n

for elem in nums:
    if elem > 2:
        for i in range(2, elem-1):
            if elem % i == 0:   #소수가 아니면
                cnt -= 1        #전체에서 빼준다
                break
    elif elem == 1:
        cnt -= 1
print(cnt)
        