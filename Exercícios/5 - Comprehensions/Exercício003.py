"""Criar uma lista com o dobro de cada número ímpar de 1 a 15."""

dobro_impar = [x * 2 for x in range(1, 16) if x % 2 != 0]
print(dobro_impar)
