cont = 0
for i in range(1, 6):
    n = int(input())
    if n % 2 == 0:
        cont += 1
if cont == 1:
    print(f'{cont} valor par')
elif cont == 0:
    print('Nenhum valor par')
else:
    print(f'{cont} valores pares')
