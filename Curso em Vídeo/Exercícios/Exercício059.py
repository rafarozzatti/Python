from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
o = 0
while o != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    o = int(input('Qual é a sua opção? '))
    if o == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif o == 2:
        print(f'A multiplicação entre {n1} x {n2} é {n1 * n2}')
    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif o == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('-=-' * 10)
    sleep(2)