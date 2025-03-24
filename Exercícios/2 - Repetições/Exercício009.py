"""Crie um programa que peça ao usuário para digitar 5 números.

Os números devem ser armazenados em uma lista.

O programa deve então ordenar os números em ordem crescente e exibir a lista ordenada."""

numeros = []

for c in range(1, 6):
    num = int(input(f'Digite o {c}º número: '))
    numeros.append(num)
numeros.sort()
print(numeros)
