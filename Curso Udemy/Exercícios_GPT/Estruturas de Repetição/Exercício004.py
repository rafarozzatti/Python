"""Crie um programa que leia um número e, utilizando um for, calcule a soma dos números de 1 até o número informado."""

num = int(input('Digite um número: '))
soma = 0
for c in range(1, num + 1):
    soma += c
print(f'A soma dos números é igual a {soma}')
