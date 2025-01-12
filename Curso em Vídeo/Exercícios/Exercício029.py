v = int(input('Qual a velocidade atual do carro? '))
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'''MULTADO! Você excedeu o limite que é de 80Km/h
Você deve pagar uma multa de R${(v - 80) * 7}!
Tenha um bom dia! Dirija com segurança!''')