#백준 2581번-소수 찾기2

m = int(input())
n = int(input())
arr = []
for i in range(m, n+1):
    arr.append(i)               #m~n 숫자 리스트
    
arr2= []

for i in range(m, n+1):
    if i == 1:
        arr2.append(i)
    for j in range(2, i):        
        if i % j == 0:
            arr2.append(i)      #소수 아닌 수 리스트
            break

arr3= []
for i in arr:
    if i not in arr2:
        arr3.append(i)          #전체에서 소수 아닌 리스트 빼서 소수 리스트 만듦

if arr3 == []:
    print(-1)
else:
    print(sum(arr3))
    print(arr3[0])