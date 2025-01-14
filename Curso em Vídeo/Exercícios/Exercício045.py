from random import randint
from time import sleep
i = ('PEDRA', 'PAPEL', 'TESOURA')
oc = randint(0, 2)
print(f'''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
o = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'''Computador jogou {i[oc]}
Jogador jogou {i[o]}''')
print('-=' * 11)
if oc == 0:
    if o == 0:
        print('EMPATE')
    elif o == 1:
        print('JOGADOR VENCE')
    else:
        print('COMPUTADOR VENCE')
if oc == 1:
    if o == 0:
        print('COMPUTADOR VENCE')
    elif o == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCE')
else:
    if o == 0:
        print('JOGADOR VENCE')
    elif o == 1:
        print('COMPUTADOR VENCE')
    else:
        print('EMPATE')