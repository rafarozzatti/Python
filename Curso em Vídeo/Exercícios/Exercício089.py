l = []
while True:
    nome = (input('Nome: '))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    m = (n1 + n2) / 2
    l.append([nome, [n1, n2], m])
    o = input('Quer continuar? [S/N] ').upper()
    if o == 'N':
        break
print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, v in enumerate(l):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
while True:
    p = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if p == 999:
        break
    if p <= len(l) - 1:
        print(f'Notas de {l[p][0]} são {l[p][1]}')