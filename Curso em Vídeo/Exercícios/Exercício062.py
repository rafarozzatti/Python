print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
m = 10
tot = 0
while m != 0:
    cont = 1
    while cont <= m:
        print(f'{t} ->', end=' ')
        t += r
        cont += 1
        tot += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {tot} termos mostrados.')