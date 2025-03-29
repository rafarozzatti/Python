nome = 'raFAel'

# Todas as letras em maiusculo
print(nome.upper())
# Todas as letras em minusculo
print(nome.lower())
# Somente a primeira letra em maiusculo
print(nome.title())

texto = ' Olá, mundo! '

print(texto + '.')
#Remove os espaços em branco
print(texto.strip() + '.')
#Remove os espaços em branco que estão a direita
print(texto.rstrip() + '.')
#Tira os espaços em branco que estão a esquerda
print(texto.lstrip() + '.')

menu  ='Python'

# Centraliza a string com 14 caracteres
print(menu.center(14))
# Centraliza a string com 14 caracteres e coloca # nos espaços
print(menu.center(14, '#'))
# Juntas a letras e coloca um pontos entre cada uma
print('.'.join(menu))
