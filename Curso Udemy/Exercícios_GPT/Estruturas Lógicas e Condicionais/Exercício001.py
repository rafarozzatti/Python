"""Peça um número ao usuário e exiba se ele é par ou ímpar."""

num = int(input('Digite um número: '))
print(f'O número {num} é PAR' if num % 2 == 0 else f'O número {num} é ÍMPAR')
