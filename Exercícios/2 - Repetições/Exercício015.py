"""Crie um programa que conte quantos dígitos um número possui.

O programa deve pedir para o usuário digitar um número e contar quantos dígitos ele tem.

Use um loop while ou for para contar os dígitos, e você pode usar a operação divisão para reduzir o número."""

cont = 0

num = int(input('Digite um número: '))
print(f'O número {num} tem ',end='')

while num > 0:
    d = num // 10
    num = d
    cont += 1
print(f'{cont} digitos')
