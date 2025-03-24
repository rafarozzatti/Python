"""Crie um programa que faça uma contagem regressiva a partir de um número fornecido pelo usuário e, a cada número, faça uma pausa de 2 segundos. No final da contagem, exiba "Feliz Ano Novo!".

A contagem deve ir de N até 1 (onde N é o número que o usuário digitar).

Use sleep(2) para pausar por 2 segundos."""

from time import sleep

num = int(input('Digite um número: '))

for c in range(num, 0, -1):
    print(c)
    sleep(2)
print('Feliz Ano Novo!')
