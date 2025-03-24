"""Crie um programa que imprima uma sequência de números começando de 1 até o número digitado pelo usuário, mas com as seguintes condições:

Se o número for múltiplo de 3, imprima "Fizz".

Se o número for múltiplo de 5, imprima "Buzz".

Se o número for múltiplo de 3 e 5, imprima "FizzBuzz".

Caso contrário, imprima o número."""

from time import sleep

num = int(input('Digite um número: '))

for c in range(1, num + 1):
    sleep(1)
    if c % 3 == 0 and c % 5 == 0:
        print('FizzBuzz')
    elif c % 3 == 0:
        print('Fizz')
    elif c % 5 == 0:
        print('Buzz')
    else:
        print(c)
