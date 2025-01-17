l = []
maior = menor = pos = 0
for i in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {i}: '))
    l.append(n)
    if i == 0:
        maior = menor = n
        pos = i
    else:
        if n > maior:
            maior = n
            pos = i
        if n < menor:
            menor = n
            pos = i
print(f'''Você digitou os valores {l}
O maior valor digitado foi {maior} na posição ''',end='')
for c, v in enumerate(l):
    if v == maior:
        print(f'{c}...',end=' ')
print(f'\nO menor valor digitado foi {menor} na posição {pos}')
for c, v in enumerate(l):
    if v == menor:
        print(f'{c}...',end=' ')