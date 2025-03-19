"""Crie uma função chamada eh_primo que recebe um número inteiro e retorna True se for primo e False caso contrário."""

def eh_primo(num): 
    if num < 2:
        return False
    
    cont = 0
    for c in range(1, num + 1):
        if num % c == 0:
            cont += 1
        if cont > 2:
            return False
    return cont == 2

n = int(input('Digite um número: '))
resposta = eh_primo(n)
if resposta:
    print(f'O número {n} É PRIMO')
else:
    print(f'O número {n} NÃO É PRIMO')
