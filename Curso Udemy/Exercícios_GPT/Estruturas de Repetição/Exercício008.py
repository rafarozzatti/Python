"""Crie um programa que leia um número e use um for para imprimir a sequência de Fibonacci até o número informado."""

num = int(input('Digite um número: '))
a, b= 0, 1
for c in range(10):
    if a > num:
        break
    print(f'{a} ',end='')
    a, b = b, a + b
