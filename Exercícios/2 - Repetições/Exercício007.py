"""Crie um programa que mostre os n primeiros números de Fibonacci.

A sequência de Fibonacci começa com os números 0 e 1, e os próximos números são a soma dos dois anteriores.

O programa deve pedir ao usuário para digitar o valor de n e imprimir os primeiros n números da sequência de Fibonacci."""

n = int(input("Digite o número de termos de Fibonacci que deseja: "))

a, b= 0, 1

while n > 0:
    print(a)
    a, b = b, a + b
    n -= 1
