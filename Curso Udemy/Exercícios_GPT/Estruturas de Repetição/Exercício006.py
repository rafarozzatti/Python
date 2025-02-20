"""Crie um programa que leia uma sequência de números até que o usuário digite o número 0. O programa deve somar todos os números digitados (não incluir o 0)."""

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    soma += num
print(f'A soma dos números é igual a {soma}')
