"""Crie uma NamedTuple chamada Produto, que armazene nome, preço e quantidade em estoque de um produto. Depois, instancie pelo menos três produtos e exiba as informações."""

from collections import namedtuple

Produto = namedtuple('Produto', ['nome', 'preco', 'quantidade'])

produtos = [
    Produto(nome='PS5', preco=3500, quantidade=1),
    Produto(nome='GTA6', preco=700, quantidade=1),
    Produto(nome='FC26', preco=350, quantidade=1)
]

for i, produto in enumerate(produtos, start=1):
    print(f'\nProduto {i}')
    print(f'Nome: {produto.nome}')
    print(f'Preço: R${produto.preco:.2f}')
    print(f'Quantidade: {produto.quantidade}')
