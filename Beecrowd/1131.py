contg = conti = conte = 0
while True:
    i, g = input().split()
    i = int(i)
    g = int(g)
    if g > i:
        contg += 1
    elif i > g:
        conti += 1
    else:
        conte += 1
    resp = int(input('Novo grenal (1-sim 2 nao)'))
    if resp == 2:
        break

print(f'''{contg + conti + conte} grenais
Inter: {conti}
Gremio: {contg}
Empates: {conte}''')
if conti > contg:
    print('Inter venceu mais')
elif conti < contg:
    print('Inter venceu mais')
else:
    print('Teve mais empates')
