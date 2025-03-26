"""Dada a lista numeros, faça o seguinte:

Ordene a lista de forma crescente e decrescente usando sorted().

Encontre o menor e o maior número usando min() e max()."""

numeros = [10, 20, 5, 40, 100, 1]

print(f'''Lista original: {numeros}
Lista em ordem crescente: {sorted(numeros)}
Lista em ordem decrescente: {sorted(numeros, reverse=True)}
Maior número da lista: {max(numeros)}
Menor número da lista: {min(numeros)}''')
