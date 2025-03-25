"""Criar um conjunto com todos os números únicos de uma lista de listas (sem duplicatas)."""

listas = [[1, 2, 3, 4], [3, 4, 5, 6], [7, 8, 9]]

conjunto = {numero for lista in listas for numero in lista}
print(conjunto)

