c1, n1, v1 = input().split()
c2, n2, v2 = input().split()
n1 = int(n1)
v1 = float(v1)
n2 = int(n2)
v2 = float(v2)
v = n1 * v1 + n2 * v2
print(f'VALOR A PAGAR: R$ {v:.2f}')
