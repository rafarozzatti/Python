"""Crie uma função chamada dados_pessoais que receba nome, idade e cidade como parâmetros nomeados e exiba essas informações formatadas."""

def dados_pessoais(**kwargs):
    for i, v in kwargs.items():
        print(f'{i}: {v}')

dados_pessoais(nome="Rafael", idade=26, cidade="São Caetano do Sul")
