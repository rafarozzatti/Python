"""Crie um programa que calcule o fatorial de um número fornecido pelo usuário.

O fatorial de um número n é o produto de todos os números de 1 até n.

Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.

O programa deve pedir ao usuário para digitar um número e, em seguida, calcular e exibir o fatorial desse número.

Se o número for 0, o fatorial é 1."""

numero = int(input("Digite um número para calcular o fatorial: "))

if numero == 0:
    print(f'O fatorial de {numero} é 1')

fat = numero

print(f'{numero}! = {numero} ',end='')

for c in range(numero - 1, 0, -1):
    fat *= c
    print(f'* {c} ' ,end='')
print(f' = {fat}')
