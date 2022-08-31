#백준 1427번-소트인사이드

import sys

num = int(sys.stdin.readline())
num_list = list(map(str, str(num)))

reversed_list = sorted(num_list, reverse=True)
new_num = "".join(reversed_list)
print(new_num)