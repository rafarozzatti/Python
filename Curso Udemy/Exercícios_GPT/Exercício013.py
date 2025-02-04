"""Peça ao usuário para digitar uma palavra e use o for para contar quantas letras a palavra possui."""

cont = 0
p = input('Digite uma palavra: ')
for l in p:
    cont += 1
print(f"A palavra '{p}' possui {cont} letras.")
