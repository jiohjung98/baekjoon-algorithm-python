#백준 9251번-LCS

import sys

alpha1 = sys.stdin.readline().strip()
alpha2 = sys.stdin.readline().strip()

alpha1_list = list(alpha1)
alpha1_list.sort()

alpha2_list = list(alpha2)
alpha2_list.sort()

for i in range(len(alpha1_list)):
    for j in range(len(alpha2_list)):
        if alpha1_list[i] == 