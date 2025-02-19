"""Simule um sistema de caixa eletrônico: peça um valor de saque e determine quantas cédulas de cada valor serão entregues (considerando notas de 100, 50, 20, 10, 5 e 2)"""

notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
valor = int(input('Digite o valor de saque: '))
if valor >= 100:
    notas100 = valor // 100
    valor = valor % 100
if valor >= 50:
    notas50 = valor // 50
    valor = valor % 50
if valor >= 20:
    notas20 = valor // 20
    valor = valor % 20
if valor >= 10:
    notas10 = valor // 10
    valor = valor % 10
if valor >= 5:
    notas5 = valor // 5
    valor = valor % 5
if valor >= 2:
    notas2 = valor // 2
print(f'{notas100} nota(s) de 100, {notas50} nota(s) de 50, {notas20} nota(s) de 20, {notas10} nota(s) de 10, {notas5} nota(s) de 5, {notas2} nota(s) de 2')
