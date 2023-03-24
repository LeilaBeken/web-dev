import math

a = int(input())
i = 1

while i != a:
    if not math.sqrt(i)%1: print(i)
    i+=1