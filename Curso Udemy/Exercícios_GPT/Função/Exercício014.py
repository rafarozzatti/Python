"""Escreva uma função ordenar_por_tamanho que recebe uma lista de palavras e retorna a lista ordenada pelo tamanho das palavras."""

def ordenar_por_tamanho(lista):
    return sorted(lista, key=len)

palavras = ["elefante", "casa", "computador", "sol", "abacaxi"]
resultado = ordenar_por_tamanho(palavras)
print(resultado)
