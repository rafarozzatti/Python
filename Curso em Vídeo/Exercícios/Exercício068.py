from random import randint
cont = 0
while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-' * 15)
    c = randint(0, 10)
    n = int(input('Diga um valor: '))
    e = input('Par ou Ímpar? [P/I] ').upper()
    print('-' * 30)
    s = n + c
    print(f'Você jogou {n} e o computador {c}. Total deu {s}', end=' ')
    if e == 'P':
        if s % 2 == 0:
            cont += 1
            print('DEU PAR')
            print('-' * 30)
            print('''Você VENCEU!
Vamos jogar novamente...''')
        else:
            print('DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU!')
            break
    if e == 'I':
        if s % 2 == 0:
            print('DEU PAR')
            print('-' * 30)
            print('Você PERDEU!')
            break
        else:
            cont += 1
            print('DEU ÍMPAR')
            print('-' * 30)
            print('''Você VENCEU!
Vamos jogar novamente...''')
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')         