"""Modifique a função saudacao para que ela receba um parâmetro chamado nome e exiba a saudação personalizada."""

def saudacao(texto):
    return f'Olá {texto}, seja bem-vindo!'

nome = input('Digite seu nome: ')

print(saudacao(nome))
