"""Criar uma nova lista onde cada elemento é uma lista de números multiplicados por 2 a partir de uma lista de listas."""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dobro = [x * 2 for lista in listas for x in lista]
print(dobro)
