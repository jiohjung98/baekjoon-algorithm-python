#백준 4673번-셀프 넘버

#방법 1: 리스트 사용
# numbers= list(range(1, 10001))
# removed_list = []
# for num in numbers:
#     for n in str(num):
#         num += int(n)
#     if num <= 10000:
#         removed_list.append(num)

# converted = set(removed_list) #set으로 바꿔서 중복 제거
# converted2 = list(converted)  #다시 list로 바꿈

# self_num = []
# for elem in numbers:
#     if elem not in converted2:
#         self_num.append(elem)

# for elem in self_num:
#     print(elem, end='\n')
    
#방법2: set 사용(더 간결함)

numbers = set(range(1, 10001))
generated_nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i <= 10000:
        generated_nums.add(i)

self_num = sorted(numbers - generated_nums)

for elem in self_num:
    print(elem)