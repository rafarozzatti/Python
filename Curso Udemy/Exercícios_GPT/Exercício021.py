"""Exercício: Crie um defaultdict que retorne "Não encontrado" para chaves ausentes."""

from collections import defaultdict
dicionario = defaultdict(lambda: "Não encontrado")
dicionario["nome"] = "Carlos"
dicionario["idade"] = 30
print(dicionario["nome"])
print(dicionario["profissao"])
