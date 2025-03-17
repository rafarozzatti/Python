"""Escreva uma função chamada soma que recebe dois números como parâmetros e retorna a soma deles."""

def soma(num1, num2):
    return num1 + num2
    
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
resultado = soma(n1, n2)
print(f'A soma entre {n1} e {n2} é igual a {resultado}')
