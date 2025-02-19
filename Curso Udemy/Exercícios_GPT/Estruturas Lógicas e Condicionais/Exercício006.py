"""Peça três números e mostre o maior e o menor entre eles."""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'{maior} é o maior número')

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'{menor} é o menor número')
