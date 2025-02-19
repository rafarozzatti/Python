"""Peça um nome de usuário e uma senha e verifique se são válidos (usuário não pode ser igual à senha)."""

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')
if usuario == senha:
    print('Dados inválidos, usuário e senha não pedem ser iguais')
elif not usuario or not senha:
    print('Erro: usuário e senha não podem ser vazios')
else:
    print('Dados válidos')
