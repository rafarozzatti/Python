import datetime

agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))
print()
hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)
hoje_formatado2 = hoje.strftime('%d/%m/%y')
print(hoje_formatado2)
print()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
print()

print(manutencao.weekday())
print()

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
if nascimento.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif nascimento.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif nascimento.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif nascimento.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif nascimento.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif nascimento.weekday() == 5:
    print('Você nasceu em um sabádo')
elif nascimento.weekday() == 6:
    print('Você nasceu em um domingo')
print()

def formata(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'
    
print(formata(hoje))
print()

nascimento2 = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento2 = datetime.datetime.strptime(nascimento2, '%d/%m/%Y')
print(nascimento2)
