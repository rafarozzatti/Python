"""Crie um programa que leia um número e, utilizando for, verifique se ele é divisível por 2, 3 e 5, imprimindo o resultado."""

num = int(input('Digite um número: '))  
divisivel = True  
for divisor in [2, 3, 5]:  
    if num % divisor != 0:  
        divisivel = False  
        break
if divisivel:  
    print(f'{num} é divisível por 2, 3 e 5.')  
else:  
    print(f'{num} não é divisível por 2, 3 e 5.')  
