from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
x = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if n == x:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {x} e não no {n}!')