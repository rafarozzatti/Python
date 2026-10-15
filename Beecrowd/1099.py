n = int(input())
for v in range(n):
    cont = 0
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y < x:
        z = -1
    else:
        z = 1
    for i in range(x + z, y, z):
        if i % 2 != 0:
            cont += i
    print(cont)
