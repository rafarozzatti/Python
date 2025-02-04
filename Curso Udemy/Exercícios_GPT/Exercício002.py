"""Peça dois números ao usuário e exiba qual é o maior. Se forem iguais, informe que são iguais."""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O maior número é {n1}')
elif n1 < n2:
    print(f'O maior número é {n2}')
else:
    print('Os números são iguais')
