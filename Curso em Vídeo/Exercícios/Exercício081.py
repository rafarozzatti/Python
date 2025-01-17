l = []
while True:
    l.append(int(input('Digite um valor: ')))
    o = input('Quer continuar? [S/N] ').upper()
    if o == 'N':
        break
l.sort(reverse=True)
print('-=' * 30)
print(f'''Você digitou {len(l)} elementos.
Os valores em ordem decrescente são {l}''')
if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')