from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
print(f'''O ângulo de {a:.1f} tem o SENO de {sin(radians(a)):.2f}
O ângulo de {a:.1f} tem o COSSENO de {cos(radians(a)):.2f}
O ângulo de {a:.1f} tem a TANGENTE de {tan(radians(a)):.2f}''')