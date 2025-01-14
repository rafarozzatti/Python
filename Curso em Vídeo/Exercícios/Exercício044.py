print(f'{'Lojas Rozzatti':=^40}')
p = float(input('Preço das compras: R$'))
print(f'''FORMAS DE PAGAMETO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 2x ou mais no cartão''')
o = int(input('Qual á a opção? '))
if o == 1:
    print(f'Sua compra de R${p:.2f} vai custar R${p * 0.9:.2f} no final.')
elif o == 2:
    print(f'Sua compra de R${p:.2f} vai custar R${p * 0.95:.2f} no final.')
elif o == 3:
    print(f'Sua compra vai custar R%{p:.2f}.')
else:
    pa = int(input('Quantas parcelas? '))
    print(f'''Sua compra será parcelada em {pa}x de R${(p * 1.2) / pa:.2f} COM JUROS.
Sua compra de R${p:.2f} vai custar R${p * 1.2:.2f} no fianl.''')