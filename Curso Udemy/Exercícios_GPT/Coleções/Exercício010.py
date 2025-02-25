"""Peça ao usuário para digitar uma frase e utilize Counter para contar quantas vezes cada palavra aparece."""

from collections import Counter
import string

frase = input('Digite uma frase: ').upper()
frase_sem_pontuacao = frase.translate(str.maketrans('', '', string.punctuation))
palavras = frase_sem_pontuacao.split()
print(Counter(palavras))
