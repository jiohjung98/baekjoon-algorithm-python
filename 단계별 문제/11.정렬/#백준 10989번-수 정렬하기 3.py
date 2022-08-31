#백준 10989번-수 정렬하기 3

#방법1- sort()함수를 쓰면 메모리가 초과됨
# import sys

# n = int(sys.stdin.readline())
# arr = []
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     arr.append(num)
    
# arr.sort()
# for elem in arr:
#     print(elem)

#방법2- 계수 정렬(카운팅 정렬)
import sys
n = int(sys.stdin.readline())
arr = [0] * 10000

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
            