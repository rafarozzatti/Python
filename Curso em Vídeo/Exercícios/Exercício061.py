print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{t} ->', end=' ')
    t += r
    cont += 1
print('FIM')