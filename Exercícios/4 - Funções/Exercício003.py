"""Modifique a função saudacao para que o nome seja opcional. Caso nenhum nome seja informado, a função deve exibir "Olá, visitante! Seja bem-vindo!"."""

def saudacao(texto='Visitante'):
    return f'Olá {texto}! Seja bem-vindo!'

nome = input('Digite seu nome: ')

print(saudacao(nome))
print(saudacao())
