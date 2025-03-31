contatos = {'nome': 'Rafael', 'telefone': '3333-2221'}

# Se o atributo informado já estiver no dicionario, imprime o valor original
print(contatos.setdefault('nome', 'Enzo'))
print(contatos)

# Se o atributo informado não estiver no dicionario, é adicionado na lista
print(contatos.setdefault('idade', 26))
print(contatos)
