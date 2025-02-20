"""Crie um programa que leia um número inteiro e, utilizando um while, conte quantos dígitos o número possui."""

cont = 0
num = int(input('Digite um número: '))
while num > 0:
    num //= 10
    cont += 1
print("O número possui", cont, "dígitos.")
