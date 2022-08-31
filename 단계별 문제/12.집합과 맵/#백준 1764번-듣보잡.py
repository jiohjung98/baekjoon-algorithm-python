# #백준 1764번-듣보잡

# import sys

# n ,m = map(int, sys.stdin.readline().split())

# arr1=[]
# arr2=[]
# for _ in range(n):
#     person = sys.stdin.readline().strip()
#     arr1.append(person)
        

# for _ in range(m):
#     person = sys.stdin.readline().strip()
#     arr2.append(person)

# answer = list(set(arr1) & set(arr2))
# answer.sort()

# print(len(answer))
# for elem in answer:
#     print(elem)


#방법2- 사전 사용
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = dict()
answer = []
for i in range(n):
    x = input().strip()
    if x not in arr1:
        arr1[x] = i         #x입력을 key값으로 저장

for i in range(m):
    y = input().strip()
    if y in arr1:           #key값에 y가 있으면(중복)
        answer.append(y)
        
answer.sort()
print(len(answer))
for elem in answer:
    print(elem)
