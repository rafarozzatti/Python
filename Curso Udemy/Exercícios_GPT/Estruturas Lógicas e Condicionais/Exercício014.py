"""Escreva um programa que receba um número de 1 a 12 (representando os meses do ano) e exiba, de acordo com o mês, a quantidade de dias do mês, considerando os anos bissextos."""

mes = int(input('Digite o número do mês: '))
ano = int(input('Digite o ano: '))
meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]

if mes in meses_31:
    print(f'{["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"][meses_31.index(mes)]} de {ano} tem 31 dias')
elif mes in meses_30:
    print(f'{["Abril", "Junho", "Setembro", "Novembro"][meses_30.index(mes)]} de {ano} tem 30 dias')
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(f'Fevereiro de {ano} tem 29 dias')
    else:
        print(f'Fevereiro de {ano} tem 28 dias')
else:
    print('Digite um mês válido')
