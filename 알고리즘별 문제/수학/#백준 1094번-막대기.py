#백준 1094번-막대기

arr = [1,2,4,8,16,32,64]
arr.sort(reverse=True)

n = int(input())
cnt = 0

for i in range(len(arr)):
    if n >= arr[i]:
        n -= arr[i]
        cnt += 1
    if n == 0:
        break

print(cnt)

        