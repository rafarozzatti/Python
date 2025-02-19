"""Desenvolva um sistema que simule um calculador de impostos baseado no salário do usuário."""

salario = float(input('Digite seu salário: '))
if salario <= 2259.2:
    print(f'O salário de R${salario} não terá cobrança de imposto')
elif salario <= 2826.65:
    print(f'O salário de R${salario} será cobrado R${(salario * 0.075) - 169.44:.2f}, 7,5%')
elif salario <= 3751.05:
    print(f'O salário de R${salario} será cobrado R${(salario * 0.15) - 381.44:.2f}, 15%')
elif salario <= 4664.68:
    print(f'O salário de R${salario} será cobrado R${(salario * 0.225) - 662.77:.2f}, 22,5%')
else:
    print(f'O salário de R${salario} será cobrado R${(salario * 0.275) - 896:.2f}, 27,5%')
