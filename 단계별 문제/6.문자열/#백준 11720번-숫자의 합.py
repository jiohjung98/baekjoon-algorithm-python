#백준 11720번-숫자의 합

n = int(input())
nums = list(input())
cnt = 0
for i in range(n):
    cnt += int(nums[i])
print(cnt)

