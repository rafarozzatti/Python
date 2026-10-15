from math import pow
con = 1
n = int(input())
for i in range(1, n + 1):
    print(f'''{i} {pow(i, 2):.0f} {pow(i, 3):.0f}
{i} {pow(i, 2) + 1:.0f} {pow(i, 3) + 1:.0f}''')
i += 1
