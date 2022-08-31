#백준 1002번-터렛

n = int(input())
list1= []
can_index1= []
list2= []
can_index2= []

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    list1.append(x1)
    list1.append(y1)
    list2.append(x2)
    list2.append(y2)
    for i in range(r1):
        for j in range(r1):
            if r1**2 == i**2 + j**2:        #r1=37, i=12, j=5, x1=0, y1=40
                list_ij = i,j
                can_index1.append(list_ij)
    for i in range(r2):
        for j in range(r2):
            if r2**2 == i**2 + j**2:        #r1=37, i=12, j=5, x1=0, y1=40
                list_ij = x2-i, y2- j
                can_index2.append(list_ij)
                
                   
print(can_index1)
print(can_index2)
print(list1)
print(list2)
    