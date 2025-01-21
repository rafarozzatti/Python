j = {}
g = []
j['nome'] = input('Nome do jogador: ')
q = int(input(f'Quantas partidas {j["nome"]} jogou? '))
for c in range(0, q):
    g.append(int(input(f' Quantos gols na partida {c}? ')))
j['gols'] = g[:]
j['total'] = sum(g)
print('-=' * 30)
print(j)
print('-=' * 30)
for k, v in j.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {j["nome"]} jogou {q} partidas.')
for i, v in enumerate(j['gols']):
    print(f'    => Na parida {i}, fez {v} gols.')
print(f'Foi um total de {j["total"]} gols.')