"""Escreva uma função gera_pares(n) que usa yield para gerar os primeiros n números pares."""

def gera_pares(n):
    num = 0
    for _ in range(n):
        yield num
        num += 2    
    
n = int(input('Quantos números pares deseja gerar? '))
pares = gera_pares(n)

for p in pares:
    print(f'{p} ',end='')
