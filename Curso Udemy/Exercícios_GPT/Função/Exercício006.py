"""Crie uma função chamada tabuada que recebe um número e imprime sua tabuada do 1 ao 10."""

def tabuada(num):
    print(f'\nTABUADA do número {n}:\n' + '-' * 15)
    for c in range(1, 11):
        print(f'{c} x {num} = {c * num}')
    print('-' * 15)

n = int(input('Digite um número: '))
tabuada(n)
