"""Crie um programa que leia uma lista de números e calcule a soma de todos os números não divisíveis por 3 ou 5, utilizando um for."""

soma = 0
lista = [65, 24, 33, 15, 21, 97, 64, 2, 17, 53]
print(f'''Lista: {lista}
Números multiplos de 3 ou 5:''',end='')
for c in lista:
    if c % 3 == 0 or c % 5 == 0:
        soma += c
        print(f' {c}',end='')
print(f'\nA soma dos números multiplos de 3 ou 5 é: {soma}')
