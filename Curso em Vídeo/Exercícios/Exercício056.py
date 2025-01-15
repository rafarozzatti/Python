cont = soma = contf = mv = hv = 0
nv = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').strip().upper()
    soma += i
    cont += 1
    if s == 'M':
        if c == 1:
            hv = i
            nv = n
        else:
            if i > hv:
                hv = i
                nv = n
    if s == 'F' and i < 20:
        contf += 1
print(f'''A média de idade do grupo é de {soma / cont:.1f} anos.
O homem mais velho tem {hv} e se chama {nv}.
Ao todo são {contf} mulheres com menos de 20 anos.''')
