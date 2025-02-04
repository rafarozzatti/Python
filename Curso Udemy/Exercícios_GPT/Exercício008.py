"""Escreva um programa que imprima uma contagem regressiva de 10 até 1 usando o for e range. Depois, imprima "Feliz Ano Novo!"."""

from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!')
