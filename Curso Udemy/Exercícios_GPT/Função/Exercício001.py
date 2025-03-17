"""Crie uma função chamada saudacao que recebe um nome como argumento e imprime "Olá, [nome]! Seja bem-vindo!".
"""

def saudacao(nome="Visitante"):
    print(f'Olá, {nome}! Seja bem-vindo!')

n = input('Digite seu nome: ').strip()
saudacao(n if n else "Visitante")
