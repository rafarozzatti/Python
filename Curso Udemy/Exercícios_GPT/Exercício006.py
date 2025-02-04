"""Crie um sistema simples de login. O usuário deve digitar um nome e senha.
Se o nome for "admin" e a senha for "1234", ele deve ser autenticado.
Se a senha estiver incorreta, exiba "Senha incorreta!".
Se o usuário não for "admin", exiba "Usuário não encontrado!".

Use not para verificar se o nome e senha estão errados."""

usuario = input('Usuário: ')
senha = input('Senha: ')
if usuario == 'admin':
    if senha == '1234':
        print('Autenticado')
    else:
        print('Senha incorreta!')
else:
    print('Usuário não encontrado!') 
