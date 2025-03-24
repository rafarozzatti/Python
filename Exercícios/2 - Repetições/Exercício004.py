"""Crie um programa que faça uma contagem regressiva de 10 a 1 usando um loop while.

O programa deve imprimir o número atual a cada iteração."""

from time import sleep

num = 10

while num > 0:
    print(num)
    sleep(1)
    num -= 1
