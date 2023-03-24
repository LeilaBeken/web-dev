a = int(input())
cnt = 0

for i in range(1, a+1) :
    if not a%i:
        cnt+=1
print(cnt)