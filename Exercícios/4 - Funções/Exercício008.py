"""Crie uma função chamada calcular_preco_final que recebe os seguintes parâmetros:

preco_base: O preço inicial de um produto.

desconto: O percentual de desconto a ser aplicado (padrão = 0).

taxa: Uma taxa adicional (padrão = 0).

**extras: Argumentos opcionais, como "cupom", "frete", etc.

A função deve calcular e retornar o preço final do produto considerando:

Aplicação do desconto

Adição da taxa

Soma dos valores extras que forem informados"""

def calcular_preco_final(preco_base, desconto=0, taxa=0, **extras):
    preco_com_desconto = preco_base - preco_base * (desconto / 100)
    return preco_com_desconto + taxa + sum(extras.values())

preco = calcular_preco_final(100, desconto=10, taxa=5, frete=15, embalagem=2)  
print(preco)  
