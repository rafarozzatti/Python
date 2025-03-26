"""Dada uma lista de números e uma lista de nomes, use o zip para combinar os itens de ambas as listas em uma sequência de tuplas, onde cada tupla contém um número e um nome. Após isso, crie um dicionário em que o número seja a chave e o nome seja o valor."""

numeros = [1, 2, 3, 4]
nomes = ["a", "b", "c", "d"]

print(dict(zip(numeros, nomes)))
