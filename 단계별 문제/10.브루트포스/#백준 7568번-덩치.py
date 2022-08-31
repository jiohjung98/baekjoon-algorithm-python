#백준 7568번-덩치

n = int(input())

data = []
grade = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

for i in range(n):
    cnt = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    grade.append(cnt)

for elem in grade:
    print(elem, end=" ")