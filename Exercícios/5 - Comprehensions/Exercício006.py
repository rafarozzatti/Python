"""Criar um dicionário a partir de uma lista de palavras, onde a chave é a palavra e o valor é o comprimento dessa palavra."""

palavras = ["abacaxi", "banana", "aviao", "laranja", "amigo"]

x =  {palavra: len(palavra) for palavra in palavras }
print(x)
