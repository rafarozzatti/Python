"""Solicite ao usuário um número e, utilizando range, imprima todos os números pares de 0 até o número fornecido."""

num = int(input('Digite um número: '))
print('Os números pares são:')
for c in range(0, num + 1):
    if c % 2 == 0:
        print(f'{c}',end='')
