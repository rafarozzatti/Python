n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2
restoDivisão = n1 % n2
divisãoInteira = n1 // n2
potencia = n1 ** n2

print(f'''\nA soma entre {n1} e {n2} é {soma}
A subtração entre {n1} e {n2} é {subtração}
A multiplicação entre {n1} e {n2} é {multiplicação}
A divisão entre {n1} e {n2} é {divisão}
O resto da divisão entre {n1} e {n2} é {restoDivisão}
A divisão inteira entre {n1} e {n2} é {divisãoInteira}
A potencia entre {n1} e {n2} é {potencia}''')
