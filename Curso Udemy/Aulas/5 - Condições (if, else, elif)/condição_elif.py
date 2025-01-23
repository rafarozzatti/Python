idade = int(input('Digite sua idade: '))
if idade < 18:
    print(f'Você tem {idade} anos. Menor de idade!')
elif idade == 18:
    print(f'Você tem {idade} anos!')
else:
    print(f'Você tem {idade} anos. Maior de idade!')