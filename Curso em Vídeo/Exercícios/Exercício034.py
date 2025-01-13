s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s * 1.1:.2f} agora.')
else:
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s * 1.15:.2f} agora.')