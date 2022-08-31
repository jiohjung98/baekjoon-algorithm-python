#백준 1193번-분수찾기

n = int(input())

line = 1
# 1 --> line = 1
# 2,3 --> line = 2
# 4,5,6 --> line = 3
# 7,8,9,10 --> line = 4

while n > line:
    n -= line
    line += 1   #n값에 따라 line 결정

y = []
z = []
for i in range(1, line+1):
    y.append(i)
    z.append(i)
    if line % 2 == 0:
        z.sort(reverse=True)
    else:
        y.sort(reverse=True)
print(f"{y[n-1]}/{z[n-1]}")
