conth = cont18 = contm20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Idade: '))
    s = input('Sexo: [M/F] ').upper()
    print('-' * 30)
    o = input('Quer continuar? [S/N] ').upper()
    if i > 18:
        cont18 += 1
    if s == 'M':
        conth +=1
    if s == 'F' and i < 20:
        contm20 += 1
    if o == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos {cont18}
Ao todo temos {conth} homens cadastrados
E temos {contm20} mulheres com menos de 20 anos''')