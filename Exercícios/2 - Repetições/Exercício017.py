"""Crie um programa que, dado um intervalo de números, encontre e imprima todos os números perfeitos nesse intervalo.

Um número perfeito é aquele que é igual à soma de seus divisores próprios (excluindo ele mesmo)."""

num1 = int(input('Digite o primeiro número do intervalo de números: '))
num2 = int(input('Digite o ultimo número do intervalo de números: '))
print('Números PERFEITOS:')

for c in range(num1, num2 + 1):
    soma = 0
    for n in range(1, c):
        if c % n == 0:
            soma += n
    if soma == c:
        print(c)
