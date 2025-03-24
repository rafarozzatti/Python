"""Peça ao usuário para digitar a idade e informe se ele é menor de idade, maior de idade ou idoso."""

idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f'Você tem {idade} anos, portanto é MENOR DE IDADE')
elif idade >= 60:
    print(f'Você tem {idade} anos, portanto é IDOSO')
else:
    print(f'Você tem {idade} anos, portanto é MAIOR DE IDADE')
