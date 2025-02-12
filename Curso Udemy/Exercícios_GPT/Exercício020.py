"""Exercício: Dado um texto, use Counter para contar a frequência de cada letra."""

from collections import Counter

texto = "Python é incrível e poderoso!"
texto_limpo = "".join(c for c in texto.upper() if c.isalnum())
print(Counter(texto_limpo))
