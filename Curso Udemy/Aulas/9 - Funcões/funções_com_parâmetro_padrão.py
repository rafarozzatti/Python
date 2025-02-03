def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial(5))
print()


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print()


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


print(mat(2, 3))
print(mat(2, 2, subtracao))
print()


total = 0
def incrementa():
    global total
    total += 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
print()


def fora():
    cont = 0
    def dentro():
        nonlocal cont
        cont += 1
        return cont
    return dentro()


print(fora())
print(fora())
print(fora())
