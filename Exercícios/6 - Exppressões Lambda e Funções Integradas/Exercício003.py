"""Dada uma lista de números, utilize map e lambda para dobrar cada número da lista."""

numeros = [1, 2, 3, 4, 5]

dobro = list(map(lambda x: x * 2, numeros))

print(dobro)
