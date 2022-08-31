#백준 1759번-암호 만들기

import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))
alphabets.sort()
     
arr= []     #전체 조합 경우의 수
for i in combinations(alphabets, l):
    arr.append(i)

answer= []

for elem in arr:
    cnt1 = 0 #모음 수 
    cnt2 = 0 #자음 수
    for i in elem:
        if i == 'a':
            cnt1 += 1
        elif i == 'e':
            cnt1 += 1
        elif i == 'i':
            cnt1 += 1
        elif i == 'o':
            cnt1 += 1
        elif i == 'u':
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        answer.append(elem)

for elem in answer:
    result1 = "".join(elem)
    print(result1)
            
print(len(answer))
                  
# acis      ..  acis
# acit      ..  acit
# aciw      ..  aciw
# acst      ..  acst
# acsw      ..  acsw
# actw      ..  actw
# aist      ..  aist
# aisw      ..  aisw
# aitw      ..  aitw
# astw      ..  astw
# cist      ..  cist
# cisw      ..  cisw
# citw      ..  citw
# istw      ..  istw

# aeioq
# aeiot
# aeiou
# aeiqt
# aeiqu
# aeitu
# aeoqt
# aeoqu
# aeotu
# aeqtu
# aioqt
# aioqu
# aiotu
# aiqtu
# aoqtu
# eioqt
# eioqu
# eiotu
# eiqtu
# eoqtu
# ioqtu


