"""Crie uma expressão lambda que receba um número e retorne o dobro dele."""
num = int(input('Digite um número: '))

dobro = lambda x: x * 2

print(f'O dobro de {num} é {dobro(num)}')
