"""Crie uma expressão lambda que receba dois números e retorne a soma deles."""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = lambda x, y: x + y

print(f'A soma entre {num1} e {num2} é {soma(num1, num2)}')
