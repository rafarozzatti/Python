"""Escreva um programa que calcule o fatorial de um número fornecido pelo usuário usando o while. Lembre-se que o fatorial de um número n é n! = n * (n-1) * (n-2) * ... * 1."""

num = int(input('Digite um número: '))
n = num
f = 1
while True:
    if n == 0:
        break
    f *= n
    n -= 1
print(f'O fatorial de {num} é {f}')
