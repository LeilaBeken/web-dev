a = int(input())
b = input().split(' ')

for i in b:
    if not int(i)%2: print(i, end=' ')