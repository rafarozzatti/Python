m= [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
sp = st = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if m[l][c] % 2 == 0:
            sp += m[l][c]
for l in range(0, 3):
    for c in range(2, 3):
        st += m[l][c]
for l in range(1, 2):
    for c in range(0, 3):
        if m[l][c] > maior:
            maior = m[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^3}]',end='')
    print()
print(f'''A soma dos valores pares é {sp}.
A soma dos valores da terceira coluna é {st}.
O maior valor da segunda linha é {maior}.''')