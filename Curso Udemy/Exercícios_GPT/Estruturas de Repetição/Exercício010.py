"""Crie um programa que leia uma senha e dê três tentativas para acertá-la. Caso a senha seja correta, exiba "Acesso permitido", caso contrário, após 3 tentativas, exiba "Acesso negado"."""

for c in range(3):
    senha = input('Digite sua senha: ')
    if senha == '1234':
        print('Acesso permitido')
        break   
else:
     print('Acesso negado')
