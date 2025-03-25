"""Criar uma lista com as palavras que começam com a letra "a" em uma lista de palavras."""

palavras = ["abacaxi", "banana", "aviao", "laranja", "amigo"]
x = [palavra for palavra in palavras if palavra.startswith('a')]
print(x)
