a = int(input())
b = input().split(' ')
cnt = 0
for i in b:
    if int(i)>0: cnt+=1
print(cnt)