"""Crie um programa que peça dois números e a operação desejada (+, -, *, /). Depois, realize o cálculo correspondente."""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    print(f'{num1:.0f} + {num2:.0f} = {num1 + num2:.0f}')
elif operacao == '-':
    print(f'{num1:.0f} - {num2:.0f} = {num1 - num2:.0f}')
elif operacao == '*':
    print(f'{num1:.0f} * {num2:.0f} = {num1 * num2:.0f}')
elif operacao == '/':
    if num2 == 0:
        print("Erro: divisão por zero não é permitida!")
    else:
        print(f'{num1:.0f} / {num2:.0f} = {num1 / num2:.2f}')
else:
    print("Operação inválida! Escolha entre +, -, * ou /")
