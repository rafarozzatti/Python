"""Exercício: Crie uma lista com 10 números inteiros e:
- Imprima o maior e o menor número.
- Ordene a lista de forma crescente e decrescente."""

numeros = [12, 5, 8, 19, 32, 3, 7, 10, 45, 1]
print(f'''Lista: {numeros}
O maior número da lista é o {max(numeros)}
O menor numero da lista é o {min(numeros)}''')
numeros_crescente = sorted(numeros)
print(f'A lista em ordem crescente: {numeros_crescente}')
numeros_decrescente =  sorted(numeros, reverse=True)
print(f'A lista em ordem decrescente: {numeros_decrescente}')
