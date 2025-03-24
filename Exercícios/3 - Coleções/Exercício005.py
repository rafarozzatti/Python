"""Utilize a classe Counter do módulo collections para contar a frequência de cada letra na palavra "programacao" e exibir o resultado."""

from collections import Counter

palavra = 'programacao'

print(Counter(palavra))
