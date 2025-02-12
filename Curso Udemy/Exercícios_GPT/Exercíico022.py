"""Exercício: Crie um OrderedDict e adicione elementos. Depois, inverta a ordem."""

from collections import OrderedDict
dicionario = OrderedDict()
dicionario["a"] = 1
dicionario["b"] = 2
dicionario["c"] = 3
dicionario["d"] = 4
dicionario["e"] = 5
print(f'Dicionário original: {dicionario}')
dicionario_invertido = OrderedDict(reversed(dicionario.items()))
print(f'Dicionário invertido: {dicionario_invertido}')
