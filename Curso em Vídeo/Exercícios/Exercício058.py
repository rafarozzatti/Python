from random import randint
cont = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
n = randint(0, 10)
p = int(input('Qual é o seu palpite? '))
while p != n:
    if p < n:
        print('Mais... Tente outra vez.')
    elif p > n:
        print('Menos... Tente outra vez.')
    cont += 1
    p = int(input('Qual é o seu palpite? '))
print(f'Acertou com {cont} tentativas. Parabéns!')