"""Escreva um programa que peça ao usuário para digitar um número e exiba se ele é positivo, negativo ou zero."""

n = int(input('Digite um número: '))
if n > 0:
    print('O número é positivo')
elif n < 0:
    print('O número é negativo')
else:
    print('O número é zero')
