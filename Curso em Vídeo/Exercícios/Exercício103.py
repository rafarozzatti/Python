def jogador(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gol = g)
else:
    jogador(n, g)