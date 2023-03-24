a = int(input())
b = list(map(int,input().split(' ')))
for i in range(a-1):
    if (b[i] > 0 and b[i+1] > 0) or (b[i] < 0 and b[i+1] < 0):
        print("YES")
        exit(0)
print("NO")