"""Escreva um programa que mostre a multiplicação de um número informado pelo usuário, começando de 1 até quando o resultado ultrapassar 100. Use o break para interromper o loop quando o resultado for maior que 100."""

n = int(input('Digite um número: '))
cont = 1
while True:
    m = n * cont
    print(f'{n} x {cont} = {m}')
    cont += 1
    if m > 100:
        break
    