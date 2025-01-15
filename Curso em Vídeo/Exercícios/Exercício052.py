cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print(c, end=' ')
    if n % c == 0:
        cont += 1
print(f'''
O número {n} foi divisível {cont} vezes''')
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')