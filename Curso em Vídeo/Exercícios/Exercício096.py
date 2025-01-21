def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m²')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Largura (m): '))
area(l, c)