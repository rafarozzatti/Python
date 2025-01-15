from datetime import date
menor =  maior = 0
an = date.today().year
for c in range(1, 8):
    a = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if an - a < 18:
        menor += 1
    else:
        maior += 1
print(f'''Ao todo tivemos {maior} pessoas maiores de idade
E também tivemos {menor} pessoas menores de idade''')