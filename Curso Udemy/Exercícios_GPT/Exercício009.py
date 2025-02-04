"""Escreva um programa que calcule a soma de todos os números pares de 1 a 100 usando o for e range."""

soma = 0
for n in range(1, 101):
    if n % 2 == 0:
        soma += n
print(f'Soma dos números pares de 1 a 100: {soma}')
