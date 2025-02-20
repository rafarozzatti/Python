"""Crie um programa que leia uma lista de números e, utilizando for, imprima o maior e o menor número dessa lista."""

lista = [25, 46, 12, 30, 20, 11, 75, 99, 17, 31]
menor = maior = lista[0]
for c in lista:
    if c < menor:
        menor = c
    if c > maior:
        maior = c
print(f'''Lista original: {lista}
Menor número da lista: {menor}
Maior número da lista: {maior}''')