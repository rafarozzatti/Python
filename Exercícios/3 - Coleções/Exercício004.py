"""Crie um conjunto chamado numeros com os seguintes valores: 1, 2, 3, 4, 5, 5, 2, 3, 6, 7.

Depois, adicione o número 8 ao conjunto e remova o número 3.

Por fim, imprima o conjunto atualizado."""

set = {1, 2, 3, 4, 5, 5, 2, 3, 6, 7}
print(f'Set original: {set}')

set.add(8)
set.discard(3)

print(f'Set atualizado: {set}')
