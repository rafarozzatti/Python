"""Use abs() para calcular o valor absoluto de todos os números na lista numeros.

Use sum() para calcular a soma de todos os números na lista numeros."""

numeros = [-1, -2, 3, 4, -5]

print(list(map(lambda x: abs(x), numeros)))
print(sum(map(lambda x: abs(x), numeros)))