#백준 1157번-단어 공부

n = input().upper()
unique_words = list(set(n))
arr= []

for elem in unique_words:
    cnt = n.count(elem)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print("?")
else:
    max_index = arr.index(max(arr))
    print(unique_words[max_index])