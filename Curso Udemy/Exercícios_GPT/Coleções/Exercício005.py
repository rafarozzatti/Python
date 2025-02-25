"""Peça ao usuário para digitar uma palavra e utilize Counter para contar quantas vezes cada letra aparece."""

from collections import Counter

palavra = input('Digite uma palavra: ').upper()
print(f'''Palavra {palavra}
Frequência das letras: {Counter(palavra)}''')
