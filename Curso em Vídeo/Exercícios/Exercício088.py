from random import randint
l = []
j = []
q = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= q:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in l:
            l.append(n)
            cont += 1
        if cont >= 6:
            break
    l.sort()
    j.append(l[:])
    l.clear()
    tot += 1
for i, v in enumerate(j):
    print(f'Jogo {i + 1}: {v}')