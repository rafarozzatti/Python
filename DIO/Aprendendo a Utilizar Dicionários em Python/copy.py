contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'idade': 26, 'telefone': '3333-2221'}
    }

# Faz uma copia do dicionario
copia = contatos.copy()
# Altera somente o valor da copia, sem alterar o dicionario original
copia['rafael@gmail.com'] = {'nome': 'Rafa'}

print(contatos['rafael@gmail.com'])
print(copia['rafael@gmail.com'])
