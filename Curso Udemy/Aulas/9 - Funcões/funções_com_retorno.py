def quadrado_de7():
    return 7 * 7


print(f'Retorno: {quadrado_de7()}')
print()


def diz_oi():
    return 'oi'


print(diz_oi())
print()


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())
print()


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(outra_funcao())
print()


from random import randint
def joga_moedas():
    valor = randint(0, 1)
    if valor > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moedas())
