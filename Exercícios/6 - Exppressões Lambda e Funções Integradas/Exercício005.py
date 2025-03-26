"""Usando filter e map, faça um programa que:

Filtre os múltiplos de 3 de uma lista de números de 1 a 20.

Multiplique os números filtrados por 2.

Exiba o resultado final."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

dobro_multiplos = list(map(lambda x: x * 2, filter(lambda x: x % 3 == 0, numeros)))

print(dobro_multiplos)
