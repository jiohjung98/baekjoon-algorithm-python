#백준 2231번- 분해합

def divide_and_sum(n):
    if n > 1:
        for i in range(1, n):
            sum_val = i
            x = 0
            i_list = list(map(int, str(i)))
            for j in range(len(i_list)):
                x += i_list[j]
            sum_val += x
            if sum_val == n:
                break
            else:
                x = 0
        if sum_val == n:
            return i
        else:
            return 0 
    else:
        return 0
    
n = int(input())
print(divide_and_sum(n))