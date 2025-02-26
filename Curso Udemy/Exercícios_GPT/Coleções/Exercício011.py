"""Peça ao usuário para digitar duas frases e exiba as palavras que aparecem apenas na primeira, mas não na segunda."""

frase1 = set(input('Digite a primeira frase: ').upper().split())
frase2 = set(input('Digite a segunda frase: ').upper().split())
print(frase1.difference(frase2))
