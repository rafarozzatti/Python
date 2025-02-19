"""Peça três lados de um triângulo e informe se ele é equilátero, isósceles ou escaleno."""

l1 = int(input('Primeiro lado do triângulo: '))
l2 = int(input('Segundo lado do triângulo: '))
l3 = int(input('Terceiro lado do triângulo: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('Triângulo Equilátero')
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Os lados fornecidos não formam um triângulo válido!')
