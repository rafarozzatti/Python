"""Crie um OrderedDict com cinco produtos e seus preços. Depois, ordene o dicionário pelo preço dos produtos e exiba o resultado."""

from collections import OrderedDict

produtos = OrderedDict([('PS5', 3500), ('FC25', 320), ('Dualshock', 300), ('GTA6', 700), ('Booster', 18)])
produtos_ordenados = OrderedDict(sorted(produtos.items(), key=lambda item: item[1]))
print(produtos_ordenados)
