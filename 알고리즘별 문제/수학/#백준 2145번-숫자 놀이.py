#백준 2145번-숫자 놀이

import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    n = str(n)
    while True:
        if len(n) == 1:
            print(n)
            break  
        else:    
            n = str(sum(list(map(int, n))))