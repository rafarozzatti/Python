from math import pow, sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {sqrt(pow(co, 2) + pow(ca, 2)):.2f}')