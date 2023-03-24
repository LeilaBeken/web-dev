def Xor(a, b):
    if a==b: return 0
    return 1

a, b = map(int, input().split())
print(Xor(a, b))