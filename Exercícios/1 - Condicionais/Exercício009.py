"""Peça ao usuário para digitar uma frase.

O programa deve contar quantas vogais e quantas consoantes a frase possui.

Considere que a, e, i, o, u são vogais e ignore os espaços e outros caracteres que não sejam letras."""

frase = input("Digite uma frase: ").strip().lower()

vogal = ['a', 'e', 'i', 'o', 'u']
contv = contc = 0

for letra in frase:
    if letra.isalpha():
        if letra in vogal:
            contv += 1
        else:
            contc += 1

print(f'A frase tem {contc} consoantes e {contv} vogais')
