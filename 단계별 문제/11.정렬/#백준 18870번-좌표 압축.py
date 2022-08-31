#백준 18870번-좌표 압축

#방법 1- index 사용(O(N)시간복잡도)- 시간초과
# --> O(N) 시간복잡도를 갖는 .index() 연산을 n번 실행하므로 O(N^2)의 시간복잡도
# import sys

# n = int(sys.stdin.readline())

# given_list = (list(map(int, sys.stdin.readline().split())))

# sorted_list = sorted(set(given_list))

# for i in range(n):
#     print(sorted_list.index(given_list[i]), end=' ')


# 방법2 - 딕셔너리 사용(딕셔너리: O(1)의 시간복잡도)
import sys

n = int(sys.stdin.readline())
given_list = (list(map(int, sys.stdin.readline().split())))

sorted_given_list = sorted(set(given_list))

dic = {}
for i in range(len(sorted_given_list)):
    dic[sorted_given_list[i]] = i

for i in range(n):
    print(dic[given_list[i]], end=' ')