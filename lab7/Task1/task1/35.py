def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

a, b = map(int, input().split(' '))
print(power(a, b))