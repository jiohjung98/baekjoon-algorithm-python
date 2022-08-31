#백준 1018번- 체스판 다시 칠하기

n, m = map(int, input().split())

# empty_list = []
# for _ in range(m):
#     arr = []
#     for _ in range(n):
#         arr.append(0)
#     empty_list.append(arr)
arr = []
for _ in range(n):
    w_or_b = list(input())
    arr.append(w_or_b)

x = 0
y = 0
for i in range(0, 8): #x=0~7
    for j in range(0, 8):
        if arr[i][j] == arr[i][j+1]:
            