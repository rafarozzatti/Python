"""Crie um dicionário onde as chaves são nomes e os valores são a quantidade de vezes que cada pessoa comprou um produto. Ordene e exiba os nomes por número de compras (do maior para o menor)."""

produtos = {'Rafael': 5, 'Enzo': 7, 'Aydana': 3, 'Adriano': 6}
ordenado = dict(sorted(produtos.items(), key=lambda item: item[1], reverse=True))
for nome, quantidade in ordenado.items():
    print(f'{nome} comprou {quantidade} vezes')
