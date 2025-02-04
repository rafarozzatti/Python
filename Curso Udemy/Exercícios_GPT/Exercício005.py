"""Peça um número ao usuário e verifique se ele é múltiplo de 3 e de 5 ao mesmo tempo.
Caso contrário, verifique se ele é múltiplo de 3 ou de 5."""

n = int(input('Digite um número: '))
if n % 3 == 0 and n % 5 == 0:
    print('O número é múltiplo de 3 e 5.')
elif n % 3 == 0 or n % 5 == 0:
    print('O número é múltiplo de 3 ou 5.')
else:
    print('O número não é múltiplo de 3 nem de 5.')
