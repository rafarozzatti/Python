from datetime import date
a = date.today().year
n = int(input('Ano de nascimento: '))
i = a - n
print(f'O atleta tem {i} anos')
if i <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif i <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif i <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif i <= 25:
    print('CLASSIFICAÇÃO: SÉNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')