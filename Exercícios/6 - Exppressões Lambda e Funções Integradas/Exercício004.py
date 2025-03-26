"""Dada uma lista de números, utilize filter e lambda para filtrar apenas os números pares."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
