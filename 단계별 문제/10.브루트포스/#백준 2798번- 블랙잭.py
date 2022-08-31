#백준 2798번- 블랙잭

n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            arr.append(nums[i]+nums[j]+nums[k])

arr2 = []

for elem in arr:
    if elem <= m:
        arr2.append(elem)
        
print(max(arr2))
