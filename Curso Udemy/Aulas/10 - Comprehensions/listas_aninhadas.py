listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(listas[0])
print(listas[0][1])
print()

for lista in listas:
    for numero in lista:
        print(numero)
print()

[[print(numero) for numero in lista] for lista in listas]
print()


tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
print()


velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
