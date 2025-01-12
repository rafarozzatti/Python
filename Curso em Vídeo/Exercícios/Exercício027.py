n = input('Digite seu nome completo: ').upper().strip().split()
print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {n[0].capitalize()}
Seu último nome é {n[len(n) - 1].capitalize()}''')