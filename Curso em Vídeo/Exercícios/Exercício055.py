maior = menor = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'''O maior peso lido foi de {maior}Kg
O menor peso lido foi de {menor}Kg''')