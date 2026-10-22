idade = 22
renda_mesal = 3000
possui_emprego = True

if idade >= 18:
    if possui_emprego:
        if renda_mesal >= 2500:
            print('Crédito aprovado')
        else:
            print('Renda insuficiente')
    else:
        print('É necesário possuir emprego')
else:
    print('Idade insuficiente')
