"""Faça uma função conta_vogais que recebe uma string e retorna a quantidade de vogais nela."""

def conta_vogais(texto):
    vogais = set('aeiouáàâãéèêíìîóòôõúùû')
    cont = sum(1 for letra in texto if letra in vogais)
    return cont

palavra = input('Digite uma palavra: ').strip().lower()
resultado = conta_vogais(palavra)
print(f'A palavra {palavra} tem {resultado} vogais')
