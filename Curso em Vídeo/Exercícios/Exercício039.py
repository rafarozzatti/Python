from datetime import date
a = date.today().year
n = int(input('Ano do nascimento: '))
i = a - n
if i < 18:
    print(f'''Quem nasceu em {n} tem {i} anos em {a}.
Ainda faltam {18 - i} anos para o alistamento.
Seu alistamento será em {(18 - i) + a}''')
elif i > 18:
    print(f'''Quem nasceu em {n} tem {i} anos em {a}.
Você deeria ter se alistado há {a - n - 18} anos.
Seu foi alistamento em {n + 18}''')
else:
    print(f'''Quem nasceu em {n} tem {i} anos em {a}.
Você deve se alistar IMEDIATAMENTE!.''')