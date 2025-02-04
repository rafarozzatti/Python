"""Escreva um programa em que o usuário tem que adivinhar um número aleatório entre 1 e 10. O programa deve pedir para o usuário tentar até acertar. Quando ele acertar, o programa deve exibir "Parabéns, você acertou!" e sair do loop usando o break."""

from random import randint
a = randint(1, 10)
while True:
    n = int(input('Tente adivinhar o número entre 1 e 10: '))
    if n == a:
        break
print('Parabéns, vcê acertou!')
