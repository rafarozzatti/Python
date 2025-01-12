n = input('Digite seu nome completo: ').strip()
s = n.split()
print(f'''Seu nome em maiúsculas é {n.upper()}
Seu nome em minúsculas é {n.lower()}
Seu nome tem ao todo {len(n) - n.count(' ')} letras
Seu primeiro nome é {s[0]} e ele tem {n.find(' ')} letras''')