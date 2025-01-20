p = []
l = []
maior = menor = 0
while True:
    l.append(input('Nome: '))
    l.append(float(input('Peso: ')))
    p.append(l[:])
    if len(p) == 1:
        maior = menor = l[1]
    else:
        if l[1] > maior:
            maior = l[1]
        if l[1] < menor:
            menor = l[1]
    l.clear()
    o = input('Quer continuar? [S/N] ').upper()
    if o == 'N':
        break
print(f'''Ao todo, você cadastrou {len(p)} pessoas.
O maior peso foi de {maior} ''',end='')
for i in p:
    if i[1] == maior:
        print(f'[{i[0]}]',end=' ')
print(f'\nO maior peso foi de {menor}Kg. Peso de ',end='')
for i in p:
    if i[1] == menor:
        print(f'[{i[0]}]',end=' ')