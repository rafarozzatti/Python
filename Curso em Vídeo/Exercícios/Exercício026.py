f = input('Digite uma frase: ').strip().upper()
print(f'''A letra A apareceu {f.count('A')} vezes na frase.
A primeira letra A apareceu na posição {f.find('A') + 1}
A última letra A apareceu na posição {f.rfind('A') + 1}''')