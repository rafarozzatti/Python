"""Crie um programa que peça um número ao usuário e, em seguida, imprima a tabuada desse número (de 1 a 10)."""

numero = int(input("Digite um número: "))

for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
