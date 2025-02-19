from random import choice

escolha = input('Pedra, Papel ou Tesoura? ').upper()
jogo = ['Pedra', 'Papel', 'Tesoura']
computador = choice(jogo).upper()
if escolha == computador:
    print(f'EMPATOU! Você jogou {escolha} e o computador jogou {computador}')
elif (escolha == 'PEDRA' and computador == 'TESOURA') or \
     (escolha == 'PAPEL' and computador == 'PEDRA') or \
     (escolha == 'TESOURA' and computador == 'PAPEL'):
    print(f'VENCEU! Você jogou {escolha} e o computador jogou {computador}')
else:
    print(f'PERDEU! Você jogou {escolha} e o computador jogou {computador}')
