"""Crie um defaultdict onde as chaves são nomes de produtos e os valores são listas de preços desses produtos ao longo do tempo. Adicione alguns preços para pelo menos três produtos diferentes e, em seguida, exiba a lista de preços de cada um."""

from collections import defaultdict

dicionario = defaultdict(list)

dicionario['PS5'].extend([3600, 3450])
dicionario['GTA6'].extend([720, 680])
dicionario['Cadeira Gamer'].extend([1250, 1100])

print(dicionario)
