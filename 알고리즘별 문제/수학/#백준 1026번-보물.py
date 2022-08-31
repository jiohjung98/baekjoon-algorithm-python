#백준 1026번-보물

n = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

sum_var = 0

for i in range(n):
    sum_var += arr_a[i] * arr_b[i]

print(sum_var)