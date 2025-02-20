"""Solicite ao usuário um número e, utilizando um loop while, imprima todos os números de 1 até o número fornecido."""

num = int(input('Digite um número: '))
cont = 1
while cont <= num:
    print(cont)
    cont += 1
