from math import pow
n = int(input())
for i in range(n):
    if i % 2 == 0:
        print(f'{i + 2}^2 = {pow(i + 2, 2):.0f}')
