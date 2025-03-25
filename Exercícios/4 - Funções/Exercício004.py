"""Crie uma função chamada soma_numeros que receba quantos números quiser e retorne a soma deles."""

def soma_numeros(*args):
    return sum(args)

print(soma_numeros(1, 2, 3, 4, 5))
print(soma_numeros(10, 20))
