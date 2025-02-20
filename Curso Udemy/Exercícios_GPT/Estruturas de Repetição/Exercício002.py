"""Crie um programa que leia um número inteiro e, utilizando um for, imprima a tabuada desse número de 1 até 10."""

num = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{num} x {c} = {c * num}')
