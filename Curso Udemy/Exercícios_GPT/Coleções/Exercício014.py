"""Crie uma NamedTuple chamada Produto, contendo os atributos nome, preco e quantidade. Depois, crie uma lista de produtos e calcule o valor total do estoque."""

from collections import namedtuple

Produto = namedtuple('Produto', 'nome preco quantidade')

produtos = [
    Produto(nome='PS5', preco=3500, quantidade=2),
    Produto(nome='DualSense', preco=350, quantidade=4),
    Produto(nome='Dunk Nike', preco=999, quantidade=5),
    Produto(nome='Booster Pokémon', preco=17.5, quantidade=12),
    Produto(nome='Figurinha Copa 2026', preco=6, quantidade=15)
]
valor_total = sum(p.preco * p.quantidade for p in produtos)
for p in produtos:
    print(f"Produto: {p.nome}, Preço unitário: R${p.preco:.2f}, Quantidade: {p.quantidade}, Valor final: R${(p.preco * p.quantidade):.2f}")
print(f"\nValor total do estoque: R${valor_total:.2f}")
