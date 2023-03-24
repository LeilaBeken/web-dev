a = int(input())

while a>1:
    if a%2:
        print("NO")
        exit(0)
    a/=2
print("YES")