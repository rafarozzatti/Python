"""Crie um programa que calcule o fatorial de um número digitado pelo usuário utilizando o loop while.

O fatorial de um número n é o produto de todos os números inteiros de 1 até n (exemplo: 5! = 5 * 4 * 3 * 2 * 1).

Use while para realizar o cálculo do fatorial."""

fat = 1

num = int(input('Digite um número para ver seu fatorial: '))
print(f'{num}! = {num}',end='')

while num > 1:
    fat *= num
    num -= 1
    print(f' * {num}',end='')
print(f' = {fat}')
