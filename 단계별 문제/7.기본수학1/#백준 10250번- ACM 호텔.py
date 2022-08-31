#백준 10250번- ACM 호텔

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    arr = []
    for i in range(1, w+1):
        for j in range(1, h+1):
            if i>= 10:
                room_num = str(j) + str(i)
            else:
                room_num = str(j)+ '0' + str(i)
            arr.append(room_num)
    print(arr[n-1])
