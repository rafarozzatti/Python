"""Peça ao usuário para digitar um número e utilize um while para contar de 1 até o número informado, exibindo cada número."""

n = int(input('Digite um número: '))
cont = 1
while cont <= n:
    print(cont)
    cont += 1
