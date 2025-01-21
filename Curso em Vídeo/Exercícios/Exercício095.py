j = {}
p = []
t = []
while True:
    j.clear()
    j['nome'] = input('Nome do jogador: ')
    q = int(input(f'Quantas partidas {j["nome"]} jogou? '))
    p.clear()
    for c in range(0, q):
        p.append(int(input(f' Quantos gols na partida {c + 1}? ')))
    j['gols'] = p[:]
    j['total'] = sum(p)
    t.append(j.copy())
    o = input('Quer continuar? [S/N] ').upper()[0]
    if o == 'N':
        break
print('-=' * 30)
print(f'cod ', end='')
for i in j.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(t):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    b = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if b == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {t[b]['nome']}!')
    for i, g in enumerate(t[b]['gols']):
        print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)