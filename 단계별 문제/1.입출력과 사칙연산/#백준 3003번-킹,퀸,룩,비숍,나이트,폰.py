#백준 3003번-킹,퀸,룩,비숍,나이트,폰

arr = [1, 1, 2, 2, 2, 8]

nums = list(map(int, input().split()))

for i in range(len(arr)):
    print(arr[i]-nums[i], end=' ')