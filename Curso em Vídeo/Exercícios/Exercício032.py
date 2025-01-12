from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
    if a % 4 == 0:
        print(f'O ano {a} é BISSEXTO')
    else:
        print(f'O ano {a} NÃO é BISSEXTO')
else:
    if a % 4 == 0 and a != 1900:
        print(f'O ano {a} é BISSEXTO')
    else:
        print(f'O ano {a} NÃO é BISSEXTO')