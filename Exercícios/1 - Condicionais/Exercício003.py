"""Peça dois números ao usuário e informe qual é o maior ou se eles são iguais."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"{num1} é maior que {num2}" if num1 > num2 else f"{num2} é maior que {num1}" if num2 > num1 else f"{num1} e {num2} são iguais")
