cont = 0
for i in range(1, 7):
    n = float(input())
    if n > 0:
        cont += 1
if cont == 1:
    print(f'{cont} valor positivo')
elif cont == 0:
    print('Nenhum valor positivo')
else:
    print(f'{cont} valores positivos')
