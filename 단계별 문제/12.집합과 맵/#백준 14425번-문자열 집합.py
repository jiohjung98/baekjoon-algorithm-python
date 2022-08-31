#백준 14425번-문자열 집합

n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    given_inputs1 = input()
    arr1.append(given_inputs1)

for _ in range(m):
    given_inputs2 = input()
    arr2.append(given_inputs2)
    

arr1.sort()
arr2.sort()
cnt = 0
for i in range(len(arr2)):
    if arr2[i] in arr1:
        cnt += 1
        if cnt == len(arr1):
            break


print(cnt)
