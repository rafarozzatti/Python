"""Exercício: Crie uma NamedTuple chamada Carro com os atributos marca, modelo e ano.
"""

from collections import namedtuple
Carro = namedtuple("Carro", ["marca", "modelo", "ano"])
porsche = Carro(marca='Porsche', modelo=911, ano=2025)
print(f'''Carro da marca {porsche.marca}, modelo {porsche.modelo}, do ano de {porsche.ano}
Dados completos: {porsche}''')
