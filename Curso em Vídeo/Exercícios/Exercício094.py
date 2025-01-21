l = []
p = {}
soma = 0
while True:
    p['nome'] = (input('Nome: '))
    p['sexo'] = (input('Sexo: [M/F] ')).upper()
    if p['sexo'] not in 'MF':
        print('Erro! Por favor, digite apenas M ou F.')
        p['sexo'] = (input('Sexo: [M/F] ')).upper()
    p['idade'] = (int(input('Idade: ')))
    soma += p['idade']
    l.append(p.copy())
    p.clear()
    o = input('Quer continuar? [S/N] ').upper()
    if  o == 'N':
        break
    elif o != 'S':
        print('ERRO! Responda apenas S ou N')
        o = input('Quer continuar? [S/N] ').upper()
m = soma / len(l)
print('-=' * 30)
print(f'''A) Ao todo temos {len(l)} cadastradas.
B) A média de idade é de {m} anos.
C) As mulheres cadastradas foram ''', end='')
for c in l:
    if c['sexo'] in 'F':
        print(f'{c['nome']} ',end='')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in l:
    if p['idade'] >= m:
        for k, v in p.items():
            print(f'    {k} = {v}; ',end='')
print('<< ENCERRADO')