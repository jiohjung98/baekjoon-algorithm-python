#백준 1541번-잃어버린 괄호

given_inputs = input().split('-') #-를 기준으로 문자열 분리 
# -> 첫 번째 문자열만 +, 나머지 문자열은 다 앞에 -가 붙음
# -> 마이너스가 없으면 given_input[0]에 모든 수 들어감
plus_var = 0
minus_var = 0

for i in given_inputs[0].split('+'):
    plus_var += int(i)
    
for i in given_inputs[1:]:
    for j in i.split('+'):
        minus_var += int(j)
        
print(plus_var-minus_var)
