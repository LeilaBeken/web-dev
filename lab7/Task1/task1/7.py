a = int(input())

if not a%400:
    print("YES")
elif not a%4 and a%100:
    print("YES")
else:
    print("NO")
