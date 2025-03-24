"""Peça ao usuário um nome de login e uma senha.

O login correto é "admin"

A senha correta é "1234"

Se ambos estiverem corretos, exiba "Acesso permitido".

Se o login estiver errado, exiba "Usuário inválido".

Se a senha estiver errada, exiba "Senha incorreta"."""

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == 'admin' and senha == '1234':
    print('Acesso permitido')
elif login != 'admin':
    print('Usuário inválido')
else:
    print('Senha incorreta')
