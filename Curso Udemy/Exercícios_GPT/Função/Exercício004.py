"""Implemente uma função fatorial que recebe um número inteiro positivo e retorna seu fatorial."""

def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    return fat

n = int(input('Digite um número: '))
resultado = fatorial(n)
print(f'O fatorial de {n} é {resultado}')
