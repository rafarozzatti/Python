c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[0;30m')


def ajuda(com):
    help(com)


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0],end='')


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = input('FUNÇÃO OU BLIBLIOTECA > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)