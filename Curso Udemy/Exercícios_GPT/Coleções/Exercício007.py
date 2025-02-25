"""Dada uma lista de palavras, utilize DefaultDict para agrupá-las por sua primeira letra."""

from collections import defaultdict

palavras = ["maçã", "banana", "abacaxi", "morango", "melancia", "amendoim", "figo"]
agrupadas = defaultdict(list)
for palavra in palavras:
    agrupadas[palavra[0]].append(palavra)
print("Palavras agrupadas pela primeira letra:")
for letra, grupo in agrupadas.items():
    print(f"{letra.upper()}: {', '.join(grupo)}")
