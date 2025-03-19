"""Crie uma função eh_anagrama que recebe duas palavras e retorna True se forem anagramas uma da outra."""

def eh_anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

palavra1 = input('Digite uma palavra: ').strip().lower()
palavra2 = input('Digite outra palavra: ').strip().lower()

if eh_anagrama(palavra1, palavra2):
    print('É um anagrama')
else:
    print('Não é um anagrama')
