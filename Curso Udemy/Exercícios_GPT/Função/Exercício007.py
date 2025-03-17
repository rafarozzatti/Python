"""Implemente uma função media_lista que recebe uma lista de números e retorna a média dos valores."""

def media_lista(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = media_lista(lista)
print(f'A média da lista {lista} é {media:.2f}')
