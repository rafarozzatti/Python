"""Crie um programa que imprima a sequência de Fibonacci invertida até o n-ésimo termo, sendo que n será o número informado pelo usuário. A sequência de Fibonacci começa com 0 e 1, e o próximo termo é a soma dos dois anteriores."""

lista = []

n = int(input("Digite o número de termos de Fibonacci que deseja: "))

a, b= 0, 1

while n > 0:
    lista.append(a)
    a, b = b, a + b
    n -= 1
lista.reverse()
print(f'Sequência Fibonacci invertida: {lista}')
