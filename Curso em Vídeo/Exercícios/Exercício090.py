d = {}
d['Nome'] = input('Nome: ')
d['Média'] = float(input('Média: '))
if d['Média'] >= 7:
    d['Situação'] = 'Aprovado'
elif d['Média'] < 7:
    d['Situação'] = 'Recuperação'
else:
    d['Situação'] = 'Reprovado'
print('-=' * 30)
print(f'''   - nome é igual a {d['Nome']}
   - média é igual a {d['Média']}
   - situação é igual a {d["Situação"]}''')
