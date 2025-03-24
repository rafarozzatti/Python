"""Crie um programa que peça ao usuário para digitar 5 números e depois calcule a soma desses números.

O programa deve imprimir o valor total da soma."""

soma = 0

for c in range(1, 6):
    num = int(input(f'Digite o {c}º número: '))
    soma += num
print(f'A soma dos números é igual a {soma}')
