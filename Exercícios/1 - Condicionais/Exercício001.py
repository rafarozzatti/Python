"""Criar um programa que recebe um número inteiro e verifica se ele é par ou ímpar."""

numero = int(input("Digite um número: "))

print(f'O número {numero} é PAR!' if numero % 2 == 0 else f'O número {numero} é ÍMPAR!')
