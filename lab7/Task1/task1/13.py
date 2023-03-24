import math as m

a = int(input())
b = int(input())

for i in range(a, b+1) :
    if not m.sqrt(i)%1:
        print(i, end=" ")