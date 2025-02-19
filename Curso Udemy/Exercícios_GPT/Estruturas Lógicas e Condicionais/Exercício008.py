"""Desenvolva um programa que calcule o IMC e diga a categoria da pessoa (exemplo: abaixo do peso, normal, sobrepeso)."""
from math import pow

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / pow(altura, 2)
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
