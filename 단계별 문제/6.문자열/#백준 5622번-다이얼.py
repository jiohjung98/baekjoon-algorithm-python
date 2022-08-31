#백준 5622번-다이얼

#방법 1- 무식한 방법
# n = input().upper()
# n = list(n)
# arr= []

# for elem in n:
#     if elem == 'A' or elem =='B' or elem =='C':
#         arr.append(3)
#     elif elem == 'D' or elem == 'E' or elem == 'F':
#         arr.append(4)
#     elif elem == 'G' or elem == 'H' or elem == 'I':
#         arr.append(5)
#     elif elem == 'J' or elem == 'K' or elem == 'L':
#         arr.append(6)
#     elif elem == 'M' or elem == 'N' or elem == 'O':
#         arr.append(7)
#     elif elem == 'P' or elem == 'Q' or elem == 'R' or elem == 'S':
#         arr.append(8)
#     elif elem == 'T' or elem == 'U' or elem == 'V':
#         arr.append(9)
#     elif elem == 'W' or elem == 'X' or elem == 'Y' or elem == 'Z':
#         arr.append(10)

# print(sum(arr))

#방법 2

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ']
n = input().upper()
time = 0

for elem in alphabet:
    for unit in elem: #리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in n:   #입력받은 문자 하나씩 분리
            if unit == x:
                time += alphabet.index(elem)
                time += 3
print(time)