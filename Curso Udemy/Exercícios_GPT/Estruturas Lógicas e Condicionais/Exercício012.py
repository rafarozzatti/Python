"""Simule um login onde o usuário tem até 3 tentativas para inserir a senha correta."""

senha = input('Insira a senha: ')
if senha == '1234':
    print('Senha correta')
else:
    print('Senha incorreta, tente novamente')
    senha = input('Insira a senha: ')
    if senha == '1234':
        print('Senha correta')
    else:
        print('Senha incorreta, tente novamente')
        senha = input('Insira a senha: ')
        if senha == '1234':
            print('Senha correta')
        else:
            print('Senha incorreta, BLOQUEADO')
