"""Crie um programa que verifique se um número fornecido pelo usuário é primo.

Um número primo é um número maior que 1 que não é divisível por nenhum número além de 1 e ele mesmo.

O programa deve perguntar ao usuário para digitar um número e verificar se ele é primo ou não.

Se o número for primo, o programa deve imprimir "O número é primo". Caso contrário, imprimir "O número não é primo"."""

cont = 0

numero = int(input("Digite um número para verificar se é primo: "))

if numero <= 1:
    print(f'O número {numero} não é primo')
else:
    for c in range(2, numero + 1):
        if numero % c == 0:
            cont += 1
    if cont == 1:
        print(f'O número {numero} é primo')
    else:
        print(f'O número {numero} não é primo')
