def quadrado(numero):
    from math import pow
    return pow(numero, 2)


print(f'Retorno: {quadrado(7):.0f}')
print(f'Retorno: {quadrado(2):.0f}')
print(f'Retorno: {quadrado(5):.0f}')
print()


def cantar_parabens(aniversariante):
    print(f'''Parabéns pra você
Nesta data querida
Muitas felicidades
Muitos anos de vida
Viva o {aniversariante}!''')
    

cantar_parabens('Rafael')
print()


def soma(a, b):
    return a + b


print(soma(2, 5))
print(soma(10, 20))
print()


def multiplica(n1, n2):
    return n1 * n2


print(multiplica(4, 5))
print(multiplica(2, 8))
print()


def outra(n1, b, msg):
    return (n1 + b) * msg


print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))
print()


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
