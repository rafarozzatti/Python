texto = input('Informe um texto: ')
vogais = 'AEIOU'

# Separa o texto em letras
for letra in texto:
    # Se letra maiuscula estiver em vogais, imprime a letra
    if letra.upper() in vogais:
        print(letra, end='')
