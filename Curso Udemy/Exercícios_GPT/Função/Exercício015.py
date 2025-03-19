"""Implemente uma função potencia(base, expoente) que calcula a potência de um número utilizando o método da exponenciação rápida.
"""

def potencia(base, expoente):
    if expoente == 0:
        return 1
    elif expoente % 2 == 0:
        metade = potencia(base, expoente // 2)
        return metade * metade
    else:
        return base * potencia(base, expoente - 1)

n1 = int(input('Digite a base: '))
n2 = int(input('Digite o expoente: '))
resultado = potencia(n1, n2)
print(f'{n1}^{n2} = {resultado}')
