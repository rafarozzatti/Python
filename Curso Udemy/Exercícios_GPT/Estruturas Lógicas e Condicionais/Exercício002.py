"""Peça um número e diga se ele é positivo, negativo ou zero."""

num = int(input('Digite um número: '))
if num > 0:
    print('O número é POSITIVO')
elif num < 0:
    print('O número é NEGATIVO')
else:
    print('O número é ZERO')
