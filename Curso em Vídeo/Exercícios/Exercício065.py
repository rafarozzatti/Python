cont = maior = menor = soma = 0
o = 'S'
while o != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    o = input('Quer continuar? [S/N] ').upper()
print(f'''Você digitou {cont} números e a media foi {soma / cont:.2f}
O maior valor foi {maior} e o menor foi {menor}''')
