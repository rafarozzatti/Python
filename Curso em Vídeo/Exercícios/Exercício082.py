l = []
li = []
lp = []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)
    o = input('Quer continuar? [S/N] ').upper()
    if o == 'N':
        break
print(f'''A lista completa é {l}
A lista de pares é {lp}
A lista de ímpares é {li}''')