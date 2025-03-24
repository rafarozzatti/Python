"""Crie um OrderedDict para armazenar nomes de clientes e a data da última compra de cada um. Adicione pelo menos quatro clientes e exiba os dados na ordem em que foram inseridos."""

from collections import OrderedDict

dicionario = OrderedDict()

dicionario['Rafael'] = '2024-03-20'
dicionario['Enzo'] = '2024-03-15'
dicionario['Aydana'] = '2024-03-10'
dicionario['Adriano'] = '2024-03-05'

print(dicionario)
