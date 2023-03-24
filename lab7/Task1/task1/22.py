import math

a = input()
b = math.pow(2, len(a)-1)
cnt = 0

for i in a:
    cnt += (int(i)*b)
    b /= 2

print(int(cnt))