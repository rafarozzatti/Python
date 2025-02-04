"""Peça um número ao usuário e verifique se ele é par ou ímpar. Use is para comparar com True ou False."""

n = int(input('Digite um número: '))
par = n % 2 == 0
if par is True:
    print('O número é par')
else:
    print('O número é ímpar')
