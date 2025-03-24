"""Crie um programa que faça uma contagem regressiva a partir de 20 até 1, imprimindo os números na tela. Quando chegar a 1, deve imprimir a mensagem "Fim da contagem!".

Use um loop para a contagem regressiva.

Use if para verificar quando a contagem chegar a 1."""

from time import sleep

for c in range(20, 0, -1):
    print(c)
    sleep(1)
    if c == 1:
        print('Fim da contagem!')
