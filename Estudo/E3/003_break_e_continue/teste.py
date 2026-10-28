cont = contnum = 0

while cont <= 9:
    num = int(input('Digite um número: '))
    cont += 1
    if num < 0:
        continue

    contnum += 1

print(f'Quantidade de números válidos: {contnum}')