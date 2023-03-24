def min(a, b, c, d):
    arr = list([a, b, c, d])
    arr.sort()
    return arr[0]

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))