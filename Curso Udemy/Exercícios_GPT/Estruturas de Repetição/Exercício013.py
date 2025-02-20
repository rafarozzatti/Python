"""Crie um programa que leia um número e utilize um while para calcular o fatorial desse número."""

fat = 1
num = int(input('Digite um número: '))
print(f'O fatorial de {num} é: {num}', end=' ')
while num >= 1:
    fat *= num
    num -= 1
    print(f'x {num}' if num >= 1 else '=',end=' ')
print(f'{fat}')
