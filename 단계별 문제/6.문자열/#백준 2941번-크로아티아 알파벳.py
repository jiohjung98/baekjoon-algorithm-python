#백준 2941번-크로아티아 알파벳

croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

for i in croatia_alpha:
    n = n.replace(i, '*')

print(len(n))