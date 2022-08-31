#백준 2908번-상수

# a, b = tuple(map(str, input().split()))

# c = list(a)
# d = list(b)

# temp1 = 0
# temp2 = 0

# temp1 = c[0]
# c[0] = c[2]
# c[2] = temp1

# temp2 = d[0]
# d[0] = d[2]
# d[2] = temp2

# e = "".join(c)
# f = "".join(d)

# print(max(e, f))


a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

print(max(a, b))