tot = tot1000 = cont = menor =0
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
b = ''
while True:
    n = input('Nome do Produto: ')
    p = float(input('Preço: R$'))
    o = input('Quer continuar? [S/N] ').upper()
    tot += p
    cont += 1
    if cont == 1:
        menor = p
        b = n
    else:
        if p < menor:
            menor = p
            b = n
    if p > 1000:
        tot1000 += 1
    if o == 'N':
        break
print(f'''O total da compra foi de R${tot:.2f}
Temos {tot1000} produtos custando mais de R$1000.00
O produto mais barato foi {b} que custa R${menor:.2f}''')
