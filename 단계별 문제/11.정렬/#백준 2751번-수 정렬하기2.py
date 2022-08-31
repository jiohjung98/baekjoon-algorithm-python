#백준 2751번-수 정렬하기2

import sys

def merge_sort(arr):
  if len(arr) < 2:
    return arr
  
  mid = len(arr) // 2
  left_arr = merge_sort(arr[:mid])
  right_arr = merge_sort(arr[mid:])
  
  merged_arr = []
  x, y = 0, 0
  while x < len(left_arr) and y < len(right_arr):
    if left_arr[x] < right_arr[y]:
      merged_arr.append(left_arr[x])
      x += 1
    else:
      merged_arr.append(right_arr[y])
      y += 1
  
  merged_arr += left_arr[x:]
  merged_arr += right_arr[y:]
  return merged_arr

given_inputs = []
n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())
  given_inputs.append(num)

given_inputs = merge_sort(given_inputs)
for elem in given_inputs:
  print(elem)
  


