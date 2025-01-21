from time import sleep


def contagem(a, b, c):
    print('-=' * 20)
    if c < 0:
        print(f'Contagem de {a} até {b} de {-c} em {-c}')
    else:
        print(f'Contagem de {a} até {b} de {c} em {c}')
    if a > b and c > 0:
        c *= -1
    for i in range(a, b + c, c):
        print(f'{i}',end=' ')
        sleep(1)
    print('FIM!')
    print('-=' * 20)


contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)