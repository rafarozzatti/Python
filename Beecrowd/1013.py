n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
maior = (n1 + n2 + abs(n1 - n2)) / 2
if n3 > maior:
    maior = n3
print(f'{maior:.0f} eh o maior')
