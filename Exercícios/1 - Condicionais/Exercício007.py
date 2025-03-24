"""Crie um programa que peça o número de um mês (1 a 12) e informe quantos dias esse mês tem.

Janeiro, março, maio, julho, agosto, setembro e dezembro têm 31 dias.

Fevereiro tem 28 dias (não leve em consideração os anos bissextos por enquanto).

Abril, junho, setembro e novembro têm 30 dias."""

mes = int(input("Digite o número do mês (1-12): "))

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes30 = [4, 6, 9, 11]
mes31 = [1, 3, 5, 7, 8, 10, 12]

if mes in mes30:
    print(f'O mês de {meses[mes - 1]} tem 30 dias')
else:
    if mes in mes31:
       print(f'O mês de {meses[mes - 1]} tem 31 dias')
    else:
        print(f'O mês {meses[mes - 1]} tem 28 dias')
