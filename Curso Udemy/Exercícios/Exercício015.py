def maior(num):
    maior = 0
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior


lista = [25, 36, 2, 75, 3, 99, 15, 12, 17]
print(f'O maior número da lista {lista} é o {maior(lista)}')
