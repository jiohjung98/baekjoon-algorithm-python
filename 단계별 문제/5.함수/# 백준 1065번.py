# 백준 1065번-한수

n = int(input())

def hansu(n):
    sum_val = 0
    for i in range(1, n+1):
        arr = list(map(int, str(i)))
        if i < 100:
            sum_val += 1
        else:
            if (arr[0]-arr[1]) == (arr[1]-arr[2]):
                sum_val += 1
    return sum_val

print(hansu(n))

            
        
                




