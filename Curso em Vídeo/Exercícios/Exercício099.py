from time import sleep


def analizando(* num):
    maior = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for v in num:
        if v > maior:
            maior = v
        print(f'{v}',end=' ')
        sleep(0.5)
    print(f'''Foram informados {len(num)} valores ao todo.
O maior valor informado foi {maior}.''')


analizando(2, 9, 4, 5, 7, 1)
analizando(4, 7, 0)
analizando(1, 2)
analizando(6)
analizando()