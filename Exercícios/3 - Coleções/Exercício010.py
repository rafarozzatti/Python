"""Crie um programa que recebe uma lista de palavras e conta a frequência de cada letra em todas as palavras combinadas.

Requisitos:

Use um Counter para contar as letras.

A entrada deve ser uma lista de palavras digitadas pelo usuário.

Exiba o dicionário com as contagens no final.

Exemplo:
Entrada: ['python', 'programacao', 'colecoes']
Saída: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 4, 'n': 2, 'r': 1, 'g': 1, 'a': 3, 'm': 1, 'c': 3, 'l': 1, 'e': 2, 's': 1}"""

from collections import Counter, OrderedDict

palavras = input("Digite palavras: ").lower().split()
juncao = (''.join(palavras))
contador = Counter(juncao)
contador_ordem = OrderedDict()
for letra in juncao:
    if letra not in contador_ordem:
        contador_ordem[letra] = contador[letra]
print(contador_ordem)
