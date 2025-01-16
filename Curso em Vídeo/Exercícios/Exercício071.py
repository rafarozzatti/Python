print('-' * 30)
print(f'{'Banco CEV':^30}')
print('-' * 30)
v = int(input('Que valor você quer sacar? R$ '))
c = 200
totc = 0
while True:
    if v >= c:
        v -= c
        totc += 1
    else:
        if totc > 0:
            print(f'Total de {totc} cédulas de R${c}')
        if c == 200:
            c = 100
        elif c == 100:
            c = 50    
        elif c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 5
        elif c == 5:
            c = 1
        totc = 0
        if v == 0:
            break