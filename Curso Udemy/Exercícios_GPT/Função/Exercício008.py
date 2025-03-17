"""Crie uma função maior_menor que recebe uma lista de números e retorna o maior e o menor número da lista."""

def maior_menor(numeros):
    if not numeros:
        return None, None
    return min(numeros), max(numeros)

lista = [11, 56, 87, 99, 103, 44, 75, 17, 23, 8]
menor, maior = maior_menor(lista)
print(f'O menor número da lista {lista} é {menor} e o maior é {maior}')
