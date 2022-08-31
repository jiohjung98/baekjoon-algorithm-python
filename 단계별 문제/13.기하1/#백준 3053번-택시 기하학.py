#백준 3053번-택시 기하학
from math import pi

n = int(input())
 
uclid = n*n*pi
taxi = n*n*2
 
print(f"{uclid:0.6f}")
print(f"{taxi:0.6f}")