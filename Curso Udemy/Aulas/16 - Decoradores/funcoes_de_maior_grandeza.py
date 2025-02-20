def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))
print()


from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(['E ai', 'Some daqui', 'Gosto muito de você'])
    return humor() + pessoa

print(cumprimento(' Enzo'))
print(cumprimento(' Rafael'))
print()


def faz_me_rir():
    def rir():
        return choice(['hahahahahahahaha', 'kkkkkkkkkkkkk', 'yayayayayayayayaya'])
    return rir

rindo = faz_me_rir()
print(rindo())
