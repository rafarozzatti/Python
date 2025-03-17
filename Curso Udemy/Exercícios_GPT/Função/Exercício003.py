"""Crie uma função chamada eh_par que recebe um número inteiro e retorna True se for par e False se for ímpar."""

def eh_par(num):
    return num % 2 == 0
    
n = int(input('Digite um número: '))
resutado = eh_par(n)
if resutado:
    print(f'O número {n} é PAR!')
else:
    print(f'O número {n} é ÍMPAR!')
