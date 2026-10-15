conta = contg = contd = 0
while True:
    n = int(input())
    if n == 1:
        conta += 1
    elif n == 2:
        contg += 1
    elif n == 3:
        contd += 1
    elif n == 4:
        break

print(f'''MUITO OBRIGADO
Alcool: {conta}
Gasolina: {contg}
Diesel: {contd}''')
