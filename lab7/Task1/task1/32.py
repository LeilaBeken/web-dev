a = int(input())
b = list(map(int,input().split(' ')))
cnt = 0
for i in range(a-1):
    if b[i] < b[i+1]: cnt+=1
print(cnt)