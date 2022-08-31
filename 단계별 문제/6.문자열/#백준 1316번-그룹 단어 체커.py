#백준 1316번-그룹 단어 체커

n = int(input())
cnt = n
for _ in range(n):  
    words = input()
    arr = []
    listed = list(words)
    for i in range(len(words)):
        if listed[i] in arr:
            if listed[i] != listed[i-1]: #그룹단어가 아니면
                cnt -= 1
                break
        arr.append(listed[i])
    
print(cnt)