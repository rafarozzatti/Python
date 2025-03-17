"""Faça uma função chamada conta_caracteres que recebe uma string e retorna a quantidade de caracteres que ela possui."""

def conta_caracteres(texto):
    return len(texto)

palavra = input('Digite uma palavra: ').strip()
resultado = conta_caracteres(palavra)
print(f'A palavra {palavra} tem {resultado} letras')
