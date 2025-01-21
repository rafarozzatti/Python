from datetime import date
a = date.today().year
d = {}
d['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
d['idade'] = a - nasc
d['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['ctps'] != 0:
    d['contratação'] = int(input('Ano de Contratação: '))
    d['salário'] = float(input('Salário: '))
    d['aposentadoria'] = d['idade'] + ((d['contratação'] + 35) - a)
print('-=' * 30)
for k, v in d.items():
    print(f'  - {k} tem o valor {v}')