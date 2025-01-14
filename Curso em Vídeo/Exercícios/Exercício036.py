v = int(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
f = int(input('Quantos anos de financiamento? '))
p = v / (12 * f)
print(f'Para pagar uma casa de R${v:.2f} em {f} anos a prestação será de R${p:.2f}')
if p <= s * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')