l = []
while True:
    n = int(input('Digite um valor: '))
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    o = input('Quer continuar? [S/N] ').upper()
    if o == 'N':
        break
l.sort()
print(f'Você digitou os valores {l}')