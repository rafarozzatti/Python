d = int(input('Qual é a distância da sua viagem? '))
if d <= 200:
    print(f'''Você está prestes a começar uma viagem de {d}Km.
E o preço da sua passagem será de R${d * 0.5:.2f}''')
else:
    print(f'''Você está prestes a começar uma viagem de {d}Km.
E o preço da sua passagem será de R${d * 0.45:.2f}''')