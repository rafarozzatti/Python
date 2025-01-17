from random import randint
cont = maior = menor = 0
l = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ',end=' ')
for i in l:
    print(f'{i}',end=' ')
print(f'''\nO maior valor sorteado foi {max(l)}
O menor valor sorteado foi {min(l)}''')
    