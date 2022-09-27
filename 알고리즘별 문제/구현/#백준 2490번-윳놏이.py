#백준 2490번-윳놏이

import sys

for _ in range(3):
    x = list(map(int, sys.stdin.readline().split()))
    result = x.count(1)

    if result == 0:
        print('D')
    elif result == 1:
        print('C')
    elif result == 2:
        print('B')
    elif result == 3:
        print('A')
    else:
        print('E')



