"""Peça ao usuário um número e exiba a tabuada desse número de 1 a 10 usando o for e range."""

n = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
