#백준 10972번-다음 순열

#방법1- permutation 사용 --> 메모리초과 
import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums = tuple(map(int, sys.stdin.readline().split()))

#모든 조합 생각

all_list = list(permutations(nums, n))
all_list.sort()
nums_index = all_list.index(nums)

if nums_index != len(all_list)-1:
    answer = all_list[nums_index+1]
    for elem in answer:
        print(elem, end=' ')
else:
    print(-1)

    