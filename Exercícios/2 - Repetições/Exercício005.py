"""Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100.

O programa deve continuar pedindo o palpite até que o usuário acerte o número secreto.

Se o usuário digitar um número maior ou menor que o número secreto, o programa deve informar se o número é maior ou menor.

O programa deve terminar quando o usuário acertar o número."""

import random

numero_secreto = random.randint(1, 100)

while True:
    num = int(input('Digite um número de 0 a 100 para adivinhar o número secreto: '))
    if num == numero_secreto:
        break
    if num > numero_secreto:
        print('O número é maior que o número secreto.')
    elif num < numero_secreto:
        print('O número é menor que o número secreto.')
print('Você acertou!')
