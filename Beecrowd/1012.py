from math import pow
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
triangulo = A * C / 2
circulo = 3.14159 * pow(C, 2)
trapezio = (A + B) * C / 2
quadrado = pow(B, 2)
retangulo = A * B
print(f'''TRIANGULO: {triangulo:.3f}
CIRCULO: {circulo:.3f}
TRAPEZIO: {trapezio:.3f}
QUADRADO: {quadrado:.3f}
RETANGULO: {retangulo:.3f}''')
