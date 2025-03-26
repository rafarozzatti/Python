"""A função reduce() do módulo functools aplica uma função a uma sequência de elementos, de forma que a função seja acumulada em cada iteração. O objetivo aqui é praticar o uso de reduce()."""

from functools import reduce

numeros = [1, 2, 3, 4, 5]

resultado = reduce(lambda x, y: x * y, numeros)

print(resultado)
