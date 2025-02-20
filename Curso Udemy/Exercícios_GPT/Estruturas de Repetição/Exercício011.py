"""Crie um programa que leia uma sequência de números até que o usuário digite um número negativo. O programa deve mostrar a soma de todos os números digitados (não incluir o número negativo)."""

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    soma += num
print(f'A soma dos números é igual a {soma}')
