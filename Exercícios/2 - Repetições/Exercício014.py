"""Crie um programa que verifique se um número digitado pelo usuário é perfeito. Um número perfeito é aquele em que a soma de seus divisores (excluindo o próprio número) é igual ao número.

Por exemplo, 6 é um número perfeito, pois seus divisores são 1, 2 e 3, e a soma de 1 + 2 + 3 = 6.

Use um loop for para verificar os divisores e somá-los."""

num = int(input('Digite um número para verificar se ele é um número perfeito: '))

soma = 0

for c in range(1, num):
    if num % c == 0:
        soma += c
if soma == num:
    print(f'O número {num} é um número perfeito')
else:
    print(f'O número {num} não é um número perfeito')
