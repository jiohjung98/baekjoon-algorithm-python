#백준 2869번-달팽이는 올라가고 싶다

# a, b, c = input().split()
# # 2  1  7
# a, b, c = int(a), int(b), int(c)
# cnt = 0
# x = 0

# while cnt <= c:
#     cnt += a
#     if cnt >= c:
#         x += 1
#         break
#     else:
#         cnt -= b
#         x += 1
# print(x)
# 시간 초과 뜸

#풀이 2
a, b, v = map(int, input().split())
k = (v-b) % (a-b)

if k == 0:
    print((v-b)//(a-b))
else:
    print(((v-b)//((a-b))+1)


