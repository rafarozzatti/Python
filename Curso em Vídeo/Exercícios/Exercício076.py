print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
l = ('Lápis', 1.75,
     'Borracha', 2,
     'Caderno', 15.90,
     'Estojo', 25,
     'Transferidor', 4.20,
     'Compasso', 9.99,
     'Mochila', 120.32,
     'Canetas', 22.30,
     'Livros', 34.98)
for p in range(0, len(l)):
    if p % 2 == 0:
        print(f'{l[p]:.<30}', end='')
    else:
        print(f'R${l[p]:>7.2f}')
print('-' * 40)
