f = 1
n = int(input('''Digite um número para
calcular seu fatorial: '''))
print(f'Calculando {n}! = {n}', end=' ')
while n != 0:
    f *= n
    n -= 1
    if n != 0:
        print(f'x {n}', end=' ')
print(f'= {f}')