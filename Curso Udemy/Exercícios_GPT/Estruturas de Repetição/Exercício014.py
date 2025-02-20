"""Crie um programa que leia uma senha e, se a senha for incorreta 3 vezes, o programa deve dar a opção de "recuperação de senha". Caso o usuário recupere a senha corretamente, ele deve ser redirecionado para a área permitida."""

for c in range(3):
    senha = input('Digite sua senha: ')
    if senha == '1234':
        print('Acesso permitido')
        break   
else:
    print('recuperação de senha')
    senha = input('Digite sua senha: ')
    if senha == '1234':
        print('área permitida')
    else:
        print('Acesso negado')
