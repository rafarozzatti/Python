contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'telefone': '3333-2221'},
    'enzo@gmail.com': {'nome': 'Enzo', 'telefone': '3443-2121'},
    'aydana@gmail.com': {'nome': 'Aydana', 'telefone': '3344-9871'},
    'adriano@gmail.com': {'nome': 'Adriano', 'telefone': '3333-7766'}
}

# Deleta o telefone de 'rafael@gmail.com'
del contatos['rafael@gmail.com']['telefone']
print(contatos)
# Deleta 'aydana@gmail.com'
del contatos['aydana@gmail.com']
print(contatos)
